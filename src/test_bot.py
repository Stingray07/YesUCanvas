import unittest
from unittest.mock import AsyncMock, Mock
from consts import help_message
import bot


class TestListenToHelp(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def test_listen_to_help():
        message = Mock()
        message.content = '!help'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        await bot.listen_to_help(message=message)

        message.channel.typing.assert_awaited_once()
        message.channel.send.assert_awaited_once_with(help_message)

    @staticmethod
    async def test_listen_to_help_never():
        message = Mock()
        message.content = '!'
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        await bot.listen_to_help(message=message)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()


class TestListenToCourses(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def listen_to_courses_never():
        message = Mock()
        message.content = "!"
        message.channel.typing = AsyncMock()
        message.channel.send = AsyncMock()

        courses = {
            'Course 1': {},
            'Course 2': {}
        }
        cache = []

        await bot.listen_to_courses(message=message, courses=courses, cache=cache)

        message.channel.typing.assert_not_awaited()
        message.channel.send.assert_not_awaited()

    # test listen to courses


if __name__ == '__main__':
    unittest.main()
