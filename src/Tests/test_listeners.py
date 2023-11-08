import unittest
from unittest.mock import AsyncMock, Mock
from src.Canvas import consts as const
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
        courses = {
            'Course 1 ID': {},
            'Course 2 ID': {}
        }
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = []

        self.assertEqual(expected_cache, actual_cache)
        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_courses_null_cache(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = {
            'Course 1 ID': {
                'course_name': 'Course 1'
            },
            'Course 2 ID': {
                'course_name': 'Course 2'
            },
        }
        cache = []

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = ['Course 1', 'Course 2']

        message.channel.typing.assert_awaited()
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [f'• **Course 1**', f'• **Course 2**']

        self.assertEqual(expected_cache, actual_cache)
        self.assertListEqual(sent_messages, expected_messages)

    async def test_listen_to_courses_with_cache(self):
        message = initialize_message(const.COURSES_COMMAND_PREFIX)
        courses = {"TEST COURSES"}       # This is to test data movement (read comment at line 6)
        cache = ['Course 1', 'Course 2']

        actual_cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = ['Course 1', 'Course 2']

        message.channel.typing.assert_awaited()
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [f'• **Course 1**', f'• **Course 2**']

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
        courses = {
            'Course ID 1': {
                'pending_assignments': {
                    "0": {
                        "name": "Assignment Name",
                        "points": 30.0,
                        "description": "Assignment Description",
                        "due": "November 18, 2023 03:59 PM",
                        "due_today": False
                    }
                },
                'course_name': "Course 1 Name"
            }
        }
        cache = {}

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = {
            'Course 1 Name': {
                '0': {
                    "name": "Assignment Name",
                    "points": 30.0,
                    "description": "Assignment Description",
                    "due": "November 18, 2023 03:59 PM",
                    "due_today": False
                }
            }
        }
        expected_sent_message = f"• **Assignment Name** \n(Course 1 Name). \nID = 0"

        self.assertEqual(expected_cache, actual_cache)
        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)

    async def test_listen_to_assignments_with_cache(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = {
            'Course 1 Name': {
                '0': {
                    "name": "Assignment Name",
                    "points": 30.0,
                    "description": "Assignment Description",
                    "due": "November 18, 2023 03:59 PM",
                    "due_today": False
                }
            }
        }

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = {
            'Course 1 Name': {
                '0': {
                    "name": "Assignment Name",
                    "points": 30.0,
                    "description": "Assignment Description",
                    "due": "November 18, 2023 03:59 PM",
                    "due_today": False
                }
            }
        }
        expected_sent_message = f"• **Assignment Name** \n(Course 1 Name). \nID = 0"

        self.assertEqual(expected_cache, actual_cache)
        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)

    async def test_listen_to_assignments_null_cache_multiple(self):
        message = initialize_message(const.ASSIGNMENTS_COMMAND_PREFIX)
        courses = {}
        cache = {
            'Course 1 Name': {
                '0': {
                    "name": "Assignment Name",
                    "points": 30.0,
                    "description": "Assignment Description",
                    "due": "November 18, 2023 03:59 PM",
                    "due_today": False
                }
            }
        }

        actual_cache = await listeners.listen_to_assignments(message=message, courses=courses, cache=cache)
        expected_cache = {
            'Course 1 Name': {
                '0': {
                    "name": "Assignment Name",
                    "points": 30.0,
                    "description": "Assignment Description",
                    "due": "November 18, 2023 03:59 PM",
                    "due_today": False
                }
            }
        }
        expected_sent_message = f"• **Assignment Name** \n(Course 1 Name). \nID = 0"

        self.assertEqual(expected_cache, actual_cache)
        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with(expected_sent_message)


if __name__ == '__main__':
    unittest.main()
