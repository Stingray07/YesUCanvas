import discord
import unittest
import os
from src.Canvas.canvas import initialize_courses
from dotenv import load_dotenv
from src.Bot import listeners as listen
from src.helper import mock, format_data

load_dotenv()
all_courses_cache = []
assignments_cache = {}
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

class TestEquality(unittest.TestCase):

    maxDiff = None
    def test_equality(self):
        courses = initialize_courses()
        mock_courses = mock
        self.assertEqual(courses, mock_courses)


def run_bot():
    print("REQUESTING COURSES FROM CANVAS...")
    courses = initialize_courses()
    print('REQUEST SUCCESSFUL')
    mock_courses = mock
    print(courses == mock_courses)
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.event
    async def on_message(message):
        global all_courses_cache
        global assignments_cache

        if message.author == bot.user:
            return

        all_courses_cache = await listen.listen_to_courses(message=message,
                                                           courses=courses,
                                                           cache=all_courses_cache)

        assignments_cache = await listen.listen_to_assignments(message=message,
                                                               courses=courses,
                                                               cache=assignments_cache)

        assignments_cache = await listen.listen_to_due_today(message=message,
                                                             courses=courses,
                                                             cache=assignments_cache)

        await listen.listen_to_teacher(message=message, courses=courses)
        await listen.listen_to_announcement(message=message, courses=courses)
        await listen.listen_to_section(message=message, courses=courses)
        await listen.listen_to_help(message=message)
        await listen.listen_to_assignment(message=message, cache=assignments_cache, courses=courses)
        await listen.listen_to_modules(message=message, courses=courses)

    bot.run(BOT_TOKEN)
