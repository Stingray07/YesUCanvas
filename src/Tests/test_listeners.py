import unittest
import discord
import copy
from html2text import html2text
from unittest.mock import AsyncMock, Mock, patch
from src.Canvas import consts as const
from src.Tests import test_consts as test_const
from src.Bot import listeners

# For some functions, I made it so that if the cache is not null, then I made its courses null.
# This is to check if the data that is being sent is actually from the cache itself, not from courses


def initialize_message(command_prefix):
    message = Mock()
    message.content = command_prefix
    message.channel.typing = AsyncMock()
    message.channel.send = AsyncMock()

    return message


class TestListenToHelp(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def test_listen_to_help():
        message = initialize_message(const.HELP_COMMAND_PREFIX)

        await listeners.listen_to_help(message=message)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(const.HELP_MESSAGE)

    @staticmethod
    async def test_listen_to_help_never():
        message = initialize_message("!")

        await listeners.listen_to_help(message=message)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()


class TestListenToCourses(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_courses_never(self):
        message = initialize_message('!')
        courses = test_const.COURSES_0
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = []

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_courses_null_cache(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = test_const.COURSES_4
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = test_const.COURSES_CACHE_1
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_COURSES_1

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertListEqual(sent_messages, expected_messages)

    async def test_listen_to_courses_with_cache(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = {"TEST COURSES"}  # This is to test data movement. I can't have it null. (read comment at line 10)
        cache = test_const.COURSES_CACHE_1

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = test_const.COURSES_CACHE_1
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_COURSES_1

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertListEqual(expected_messages, sent_messages)

    async def test_listen_to_courses_null_courses(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = {}
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = []

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with('COURSES NOT FOUND')
        self.assertEqual(expected_cache, actual_cache)


class TestListenToAssignments(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_assignments_never(self):
        message = initialize_message("!")
        courses = {}
        cache = []

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = []

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = test_const.COURSES_3
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_2
        expected_sent_message = test_const.EXPECTED_SENT_ASSIGNMENTS_0[0]

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = test_const.ASSIGNMENTS_2

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_2
        expected_sent_message = test_const.EXPECTED_SENT_ASSIGNMENTS_0[0]

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_multiple_course(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = test_const.COURSES_4
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_3
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_2

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)

    async def test_listen_to_assignments_with_cache_multiple_course(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = test_const.ASSIGNMENTS_3

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_3
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_2

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)

    async def test_listen_to_assignments_null_cache_multiple_assignments_one_course(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = test_const.COURSES_5
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_4
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_1

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)

    async def test_listen_to_assignments_with_cache_multiple_assignments_one_course(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = test_const.ASSIGNMENTS_4

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_4
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_1

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)

    async def test_listen_to_assignments_null_cache_multiple_assignments_multiple_course(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = test_const.COURSES_6
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_5
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_3

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)

    async def test_listen_to_assignments_with_cache_multiple_assignments_multiple_course(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = test_const.ASSIGNMENTS_5

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_5
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_3

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)


class TestListenToAssignment(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_assignment_never(self):
        message = initialize_message("!")
        courses = {}
        cache = {}

        actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
        expected_cache = {}

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignment_bad_id(self):
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + '?')
        courses = test_const.COURSES_3
        cache = {}

        actual_cache = await listeners.listen_to_assignment(message=message, courses=courses, cache=cache)
        expected_cache = test_const.ASSIGNMENTS_2

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_once_with("ID NOT FOUND")
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignment_prefix_spaces_null_cache(self):
        assignment_id = '    Assignment ID 1'
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + assignment_id)
        courses = test_const.COURSES_3
        cache = {}

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
            expected_cache = test_const.ASSIGNMENTS_2

            actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list if call.args]
            expected_sent_messages = test_const.EXPECTED_SENT_ASSIGNMENT_1

            message.channel.typing.assert_awaited()
            mock_embed.assert_called_with(
                title='**DESCRIPTION**',
                description=html2text('Assignment Description 1')
            )
            self.assertEqual(expected_cache, actual_cache)
            self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_assignment_prefix_spaces_with_cache(self):
        assignment_id = '      Assignment ID 1'
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + assignment_id)
        courses = {}
        cache = test_const.ASSIGNMENTS_2

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
            expected_cache = test_const.ASSIGNMENTS_2

            actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list if call.args]
            expected_sent_messages = test_const.EXPECTED_SENT_ASSIGNMENT_1

            message.channel.typing.assert_awaited()
            mock_embed.assert_called_with(
                title='**DESCRIPTION**',
                description=html2text('Assignment Description 1')
            )
            self.assertEqual(expected_cache, actual_cache)
            self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_assignment_null_cache(self):
        assignment_id = 'Assignment ID 1'
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + assignment_id)
        courses = test_const.COURSES_3
        cache = {}

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
            expected_cache = test_const.ASSIGNMENTS_2

            actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list if call.args]
            expected_send_messages = test_const.EXPECTED_SENT_ASSIGNMENT_1

            message.channel.typing.assert_awaited()
            mock_embed.assert_called_with(
                title='**DESCRIPTION**',
                description=html2text('Assignment Description 1')
            )
            self.assertEqual(expected_send_messages, actual_sent_messages)
            self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignment_with_cache(self):
        assignment_id = 'Assignment ID 1'
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + assignment_id)
        courses = {}
        cache = test_const.ASSIGNMENTS_2

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
            expected_cache = test_const.ASSIGNMENTS_2

            actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list if call.args]
            expected_sent_messages = test_const.EXPECTED_SENT_ASSIGNMENT_1

            message.channel.typing.assert_awaited()
            mock_embed.assert_called_with(
                title='**DESCRIPTION**',
                description=html2text('Assignment Description 1')
            )
            self.assertEqual(expected_sent_messages, actual_sent_messages)
            self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignment_null_cache_multiple(self):
        assignment_id = 'Assignment ID 2'
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + assignment_id)
        courses = test_const.COURSES_5
        cache = {}

        with patch.object(discord,  'Embed', Mock()) as mock_embed:
            actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
            expected_cache = test_const.ASSIGNMENTS_4

            actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list if call.args]
            expected_sent_messages = test_const.EXPECTED_SENT_ASSIGNMENT_2

            message.channel.typing.assert_awaited()
            mock_embed.assert_called_with(
                title='**DESCRIPTION**',
                description=html2text('Assignment Description 2')
            )
            self.assertEqual(expected_sent_messages, actual_sent_messages)
            self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignment_with_cache_multiple(self):
        assignment_id = 'Assignment ID 2'
        message = initialize_message(const.ASSIGNMENT_COMMAND_PREFIX + assignment_id)
        courses = {}
        cache = test_const.ASSIGNMENTS_4

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            actual_cache = await listeners.listen_to_assignment(message=message, cache=cache, courses=courses)
            expected_cache = test_const.ASSIGNMENTS_4

            actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list if call.args]
            expected_sent_messages = test_const.EXPECTED_SENT_ASSIGNMENT_2

            message.channel.typing.assert_awaited()
            mock_embed.assert_called_with(
                title='**DESCRIPTION**',
                description=html2text('Assignment Description 2')
            )
            self.assertEqual(expected_sent_messages, actual_sent_messages)
            self.assertEqual(expected_cache, actual_cache)


class TestListenToTeacher(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_teacher_never(self):
        message = initialize_message("!")
        courses = {}

        await listeners.listen_to_teacher(message=message, courses=courses)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_teacher_prefix_spaces(self):
        course_key = '    Course Key 1'
        message = initialize_message(const.TEACHER_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        await listeners.listen_to_teacher(message=message, courses=courses)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with('**Teacher 1**')

    async def test_listen_to_teacher(self):
        course_key = 'Course Key 1'
        message = initialize_message(const.TEACHER_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        await listeners.listen_to_teacher(message=message, courses=courses)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with('**Teacher 1**')

    async def test_listen_to_teacher_bad_key(self):
        course_key = '?'
        message = initialize_message(const.TEACHER_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        await listeners.listen_to_teacher(message=message, courses=courses)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with('Course Code Not Found')

    async def test_listen_to_teacher_multiple(self):
        course_key = 'Course Key 2'
        message = initialize_message(const.TEACHER_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_4

        await listeners.listen_to_teacher(message=message, courses=courses)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with('**Teacher 2**')


class TestListenToAnnouncement(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_announcement_never(self):
        message = initialize_message("!")
        courses = {}

        await listeners.listen_to_announcement(message=message, courses=courses)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_announcement(self):
        course_key = 'Course Key 1'
        message = initialize_message(const.ANNOUNCEMENT_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            await listeners.listen_to_announcement(message=message, courses=courses)
            expected_sent_message = test_const.EXPECTED_SENT_ANM_1

            message.channel.typing.assert_awaited_once()
            mock_embed.assert_called_with(description=f"{html2text(expected_sent_message)}")

    async def test_listen_to_announcement_prefix_spaces(self):
        course_key = '    Course Key 1'
        message = initialize_message(const.ANNOUNCEMENT_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            await listeners.listen_to_announcement(message=message, courses=courses)
            expected_sent_message = test_const.EXPECTED_SENT_ANM_1

            message.channel.typing.assert_awaited_once()
            mock_embed.assert_called_with(description=f"{html2text(expected_sent_message)}")

    async def test_listen_to_announcement_bad_key(self):
        course_key = '?'
        message = initialize_message(const.ANNOUNCEMENT_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            await listeners.listen_to_announcement(message=message, courses=courses)
            expected_sent_message = 'Course Code Not Found'

            message.channel.typing.assert_awaited_once()
            mock_embed.assert_called_with(description=f"{html2text(expected_sent_message)}")

    async def test_listen_to_announcement_multiple(self):
        course_key = 'Course Key 2'
        message = initialize_message(const.ANNOUNCEMENT_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_4

        with patch.object(discord, 'Embed', Mock()) as mock_embed:
            await listeners.listen_to_announcement(message=message, courses=courses)
            expected_sent_message = test_const.EXPECTED_SENT_ANM_2

            message.channel.typing.assert_awaited_once()
            mock_embed.assert_called_with(description=f"{html2text(expected_sent_message)}")


class TestListenToSection(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_section_never(self):
        message = initialize_message("!")
        courses = {}

        await listeners.listen_to_announcement(message=message, courses=courses)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_section(self):
        course_key = 'Course Key 1'
        message = initialize_message(const.SECTION_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        await listeners.listen_to_section(message=message, courses=courses)
        expected_sent_message = test_const.EXPECTED_SENT_SECTION_1

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(expected_sent_message)

    async def test_listen_to_section_prefix_spaces(self):
        course_key = '    Course Key 1'
        message = initialize_message(const.SECTION_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        await listeners.listen_to_section(message=message, courses=courses)
        expected_sent_message = test_const.EXPECTED_SENT_SECTION_1

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(expected_sent_message)

    async def test_listen_to_section_bad_key(self):
        course_key = '?'
        message = initialize_message(const.SECTION_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_3

        await listeners.listen_to_section(message=message, courses=courses)
        expected_sent_message = '**Section Not Found**'

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(expected_sent_message)

    async def test_listen_to_section_multiple(self):
        course_key = 'Course Key 2'
        message = initialize_message(const.SECTION_COMMAND_PREFIX + course_key)
        courses = test_const.COURSES_4

        await listeners.listen_to_section(message=message, courses=courses)
        expected_sent_message = test_const.EXPECTED_SENT_SECTION_2

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(expected_sent_message)


class TestListenToDueToday(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_due_today_never(self):
        message = initialize_message("!")
        courses = {}
        assignments_cache = {}

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = {}

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_due_today(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = test_const.COURSES_3

        assignments_cache = {}

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_2
        expected_message = test_const.EXPECTED_SENT_ASSIGNMENTS_0[0]

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_once_with(expected_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_not_due_today(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = copy.deepcopy(test_const.COURSES_3)
        courses['COURSE KEY 1']['pending_assignments']['Assignment ID 1']['due_today'] = False
        assignments_cache = {}

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = copy.deepcopy(test_const.ASSIGNMENTS_2)
        expected_cache['Course Name 1']['Assignment ID 1']['due_today'] = False
        expected_message = 'No Due Today'

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_once_with(expected_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache_due_today(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = {}
        assignments_cache = test_const.ASSIGNMENTS_2

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_2
        expected_message = test_const.EXPECTED_SENT_ASSIGNMENTS_0[0]

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_once_with(expected_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache_not_due_today(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = {}
        assignments_cache = copy.deepcopy(test_const.ASSIGNMENTS_2)
        assignments_cache['Course Name 1']['Assignment ID 1']['due_today'] = False

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = copy.deepcopy(test_const.ASSIGNMENTS_2)
        expected_cache['Course Name 1']['Assignment ID 1']['due_today'] = False
        expected_message = 'No Due Today'

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_once_with(expected_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_multiple_course(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = test_const.COURSES_4
        assignments_cache = {}

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_3
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_message = test_const.EXPECTED_SENT_ASSIGNMENTS_2

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_message, sent_messages)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache_multiple_course(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = {}
        assignments_cache = test_const.ASSIGNMENTS_3

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_3
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_message = test_const.EXPECTED_SENT_ASSIGNMENTS_2

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_message, sent_messages)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_multiple_assignment_one_course(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = test_const.COURSES_5
        assignments_cache = {}

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_4
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_message = test_const.EXPECTED_SENT_ASSIGNMENTS_1

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_message, sent_messages)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache_multiple_assignment_one_course(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = {}
        assignments_cache = test_const.ASSIGNMENTS_4

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_4
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_1

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_messages, sent_messages)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_multiple_assignment_multiple_course(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = test_const.COURSES_6
        assignments_cache = {}

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_5
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_3

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_messages, sent_messages)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache_multiple_assignment_multiple_course(self):
        message = initialize_message(const.DUE_TODAY_COMMAND_PREFIX)
        courses = {}
        assignments_cache = test_const.ASSIGNMENTS_5.copy()

        actual_cache = await listeners.listen_to_due_today(message=message, courses=courses, cache=assignments_cache)
        expected_cache = test_const.ASSIGNMENTS_5
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = test_const.EXPECTED_SENT_ASSIGNMENTS_3

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_messages, sent_messages)
        self.assertEqual(expected_cache, actual_cache)


class TestListenToAllModules(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_all_modules_never(self):
        message = initialize_message("!")
        courses = {}

        await listeners.listen_to_modules(message=message, courses=courses)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_all_modules_bad_id(self):
        course_id = "?"
        message = initialize_message(const.MODULES_COMMAND_PREFIX + course_id)
        courses = {}

        await listeners.listen_to_modules(message=message, courses=courses)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with('COURSE NOT FOUND')

    async def test_listen_to_modules_one_course(self):
        course_id = 'COURSE KEY 1'
        message = initialize_message(const.MODULES_COMMAND_PREFIX + course_id)
        courses = test_const.COURSES_3

        await listeners.listen_to_modules(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULES_0
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_modules_multiple_course(self):
        course_id = 'COURSE KEY 1'
        message = initialize_message(const.MODULES_COMMAND_PREFIX + course_id)
        courses = test_const.COURSES_4

        await listeners.listen_to_modules(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULES_0
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_modules_multiple_modules_one_course(self):
        course_id = 'COURSE KEY 1'
        message = initialize_message(const.MODULES_COMMAND_PREFIX + course_id)
        courses = test_const.COURSES_5

        await listeners.listen_to_modules(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULES_1
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_modules_multiple_modules_multiple_course(self):
        course_id = 'COURSE KEY 1'
        message = initialize_message(const.MODULES_COMMAND_PREFIX + course_id)
        courses = test_const.COURSES_5

        await listeners.listen_to_modules(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULES_1
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)


class TestListenToModule(unittest.IsolatedAsyncioTestCase):
    module_id = 'Module ID 1'

    async def test_listen_to_module_never(self):
        message = initialize_message("!")
        courses = {}

        await listeners.listen_to_module(message=message, courses=courses)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_all_module_bad_id(self):
        module_id = '?'
        message = initialize_message(const.MODULE_COMMAND_PREFIX + module_id)
        courses = test_const.COURSES_3

        await listeners.listen_to_module(message=message, courses=courses)

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_once_with('MODULE NOT FOUND')

    async def test_listen_to_module_one_course(self):
        message = initialize_message(const.MODULE_COMMAND_PREFIX + self.module_id)
        courses = test_const.COURSES_3

        await listeners.listen_to_module(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULE_0
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_module_multiple_course(self):
        module_id = 'Module ID 2'
        message = initialize_message(const.MODULE_COMMAND_PREFIX + module_id)
        courses = test_const.COURSES_4

        await listeners.listen_to_module(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULE_1
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_module_multiple_modules_one_course(self):
        message = initialize_message(const.MODULE_COMMAND_PREFIX + self.module_id)
        courses = test_const.COURSES_5

        await listeners.listen_to_module(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULE_0
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)

    async def test_listen_to_module_multiple_modules_multiple_course(self):
        module_id = 'Module ID 4'
        message = initialize_message(const.MODULE_COMMAND_PREFIX + module_id)
        courses = test_const.COURSES_6

        await listeners.listen_to_module(message=message, courses=courses)
        expected_sent_messages = test_const.EXPECTED_SENT_MODULE_2
        actual_sent_messages = [call[0][0] for call in message.channel.send.call_args_list]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_sent_messages, actual_sent_messages)


if __name__ == '__main__':
    unittest.main()
