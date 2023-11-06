import unittest
from unittest.mock import AsyncMock, Mock
from src.Canvas.consts import HELP_MESSAGE
from src.Bot import listeners as listen


class TestListenToHelp(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def test_listen_to_help():
        message = Mock()
        message.content = '!help'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        await listen.listen_to_help(message=message)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(HELP_MESSAGE)

    @staticmethod
    async def test_listen_to_help_never():
        message = Mock()
        message.content = '!'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        await listen.listen_to_help(message=message)

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
            'Course 1': {},
            'Course 2': {}
        }
        cache = []

        await listen.listen_to_courses(message=message, courses=courses, cache=cache)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    @staticmethod
    async def test_listen_to_courses_null_cache():
        message = Mock()
        message.content = "!courses"
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        courses = {
            'Course 1': {
                'course_name': 'Course 1'
            },
            'Course 2': {
                'course_name': 'Course 2'
            }
        }
        cache = []

        await listen.listen_to_courses(message=message, courses=courses, cache=cache)

        message.channel.typing.assert_awaited()
        message.channel.send.assert_awaited()


if __name__ == '__main__':
    unittest.main()
