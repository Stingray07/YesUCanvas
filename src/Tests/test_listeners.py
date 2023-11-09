import unittest
from unittest.mock import AsyncMock, Mock
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
        courses = test_const.course_0
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = []

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_courses_null_cache(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = test_const.course_4
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = ['Course Name 1', 'Course Name 2']
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [f'• **Course Name 1**', f'• **Course Name 2**']

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertListEqual(sent_messages, expected_messages)

    async def test_listen_to_courses_with_cache(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = {"TEST COURSES"}  # This is to test data movement. I can't have it null. (read comment at line 6)
        cache = ['Course Name 1', 'Course Name 2']

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = ['Course Name 1', 'Course Name 2']
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [f'• **Course Name 1**', f'• **Course Name 2**']

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
        courses = test_const.course_3
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.assignments_2
        expected_sent_message = f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1"

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_with_cache(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = test_const.assignments_2

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.assignments_2
        expected_sent_message = f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1"

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)
        self.assertEqual(expected_cache, actual_cache)

    async def test_listen_to_assignments_null_cache_multiple(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = test_const.course_4
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.assignments_3
        expected_sent_message_1 = f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1"
        expected_sent_message_2 = f"• **Assignment Name 2** \n(Course Name 2). \nID = Assignment ID 2"
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [expected_sent_message_1, expected_sent_message_2]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)

    async def test_listen_to_assignments_with_cache_multiple(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = test_const.assignments_3

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = test_const.assignments_3
        expected_sent_message_1 = f"• **Assignment Name 1** \n(Course Name 1). \nID = Assignment ID 1"
        expected_sent_message_2 = f"• **Assignment Name 2** \n(Course Name 2). \nID = Assignment ID 2"
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [expected_sent_message_1, expected_sent_message_2]

        message.channel.typing.assert_awaited()
        self.assertEqual(expected_cache, actual_cache)
        self.assertEqual(expected_messages, sent_messages)


class TestListenToAssignment(unittest.IsolatedAsyncioTestCase):

    async def test_listen_to_assignment_never(self):
        message = initialize_message("!")
        cache = {}

        actual_cache = await listeners.listen_to_assignment(message=message, cache=cache)
        expected_cache = None

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()
        self.assertEqual(expected_cache, actual_cache)


if __name__ == '__main__':
    unittest.main()
