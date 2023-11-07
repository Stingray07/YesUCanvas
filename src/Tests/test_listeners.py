import unittest
from unittest.mock import AsyncMock, Mock
from src.Canvas.consts import HELP_MESSAGE
from src.Bot import listeners


class TestListenToHelp(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def test_listen_to_help():
        message = Mock()
        message.content = '!help'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        await listeners.listen_to_help(message=message)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(HELP_MESSAGE)

    @staticmethod
    async def test_listen_to_help_never():
        message = Mock()
        message.content = '!'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        await listeners.listen_to_help(message=message)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()


class TestListenToCourses(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def test_listen_to_courses_never():
        message = Mock()
        message.content = "!"
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        courses = {
            'Course 1 ID': {},
            'Course 2 ID': {}
        }
        cache = []

        await listeners.listen_to_courses(message=message, courses=courses, cache=cache)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    async def test_listen_to_courses_null_cache(self):
        message = Mock()
        message.content = "!courses"
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        courses = {
            'Course 1 ID': {
                'course_name': 'Course 1'
            },
            'Course 2 ID': {
                'course_name': 'Course 2'
            },
        }
        cache = []

        cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = ['Course 1', 'Course 2']

        message.channel.typing.assert_awaited()
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [f'• **Course 1**', f'• **Course 2**']

        self.assertEqual(expected_cache, cache)
        self.assertListEqual(sent_messages, expected_messages)

    async def test_listen_to_courses_with_cache(self):
        message = Mock()
        message.content = '!courses'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        courses = {
            'Course 1 ID': {
                'course_name': 'Course 1'
            },
            'Course 2 ID': {
                'course_name': 'Course 2'
            }
        }
        cache = ['Course 1', 'Course 2']

        cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = ['Course 1', 'Course 2']

        message.channel.typing.assert_awaited()
        sent_messages = [call[0][0] for call in message.channel.send.call_args_list]
        expected_messages = [f'• **Course 1**', f'• **Course 2**']

        self.assertEqual(cache, expected_cache)
        self.assertListEqual(expected_messages, sent_messages)

    async def test_listen_to_courses_null_courses(self):
        message = Mock()
        message.content = '!courses'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        courses = {}
        cache = []

        cache = await listeners.listen_to_courses(message=message, courses=courses, cache=cache)
        expected_cache = []
        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited_with('COURSES NOT FOUND')

        self.assertEqual(expected_cache, cache)


if __name__ == '__main__':
    unittest.main()
