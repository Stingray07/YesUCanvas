import discord
import os
from src.Canvas.canvas import initialize_courses
from dotenv import load_dotenv
from src.Bot import listeners as listen
from src.helper import mock

load_dotenv()
all_courses_cache = []
assignments_cache = {}
due_today_cache = {}


def run_bot():
    print("REQUESTING COURSES FROM CANVAS...")
    courses = mock
    # courses = initialize_courses()
    # format_data(courses)
    BOT_TOKEN = os.getenv('DISCORD_TOKEN')
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
        global due_today_cache

        if message.author == bot.user:
            return

        all_courses_cache = await listen.listen_to_courses(message=message, courses=courses, cache=all_courses_cache)
        assignments_cache = await listen.listen_to_assignments(message=message, courses=courses,
                                                               cache=assignments_cache)
        due_today_cache = await listen.listen_to_due_today(message=message,
                                                           courses=courses,
                                                           assignments_cache=assignments_cache,
                                                           due_today_cache=due_today_cache)
        await listen.listen_to_teacher(message=message, courses=courses)
        await listen.listen_to_announcement(message=message, courses=courses)
        await listen.listen_to_section(message=message, courses=courses)
        await listen.listen_to_help(message=message)
        await listen.listen_to_assignment(message=message, cache=assignments_cache, courses=courses)

    bot.run(BOT_TOKEN)
