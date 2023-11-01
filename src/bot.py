import discord
import os
from html2text import html2text
from canvas import initialize_courses, format_data
from helper import mock
import course_functions as cf
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
all_courses_cache = []
assignments_cache = {}
due_today_cache = {}


def run_bot():
    print("REQUESTING COURSES FROM CANVAS API...")
    courses = mock
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

        all_courses_cache = await listen_to_courses(message=message, courses=courses, cache=all_courses_cache)
        assignments_cache = await listen_to_assignments(message=message, courses=courses, cache=assignments_cache)
        await listen_to_teacher(message=message, courses=courses)
        await listen_to_announcement(message=message, courses=courses)
        await listen_to_section(message=message, courses=courses)
        await listen_to_help(message=message)
        due_today_cache = await listen_to_due_today(message=message,
                                                    courses=courses,
                                                    pending_assignments=assignments_cache,
                                                    cache=due_today_cache)

    bot.run(BOT_TOKEN)


async def listen_to_help(message):
    if message.content.startswith('!help'):
        await message.channel.typing()
        msg = '''**Available Commands:**
                - `!courses`: Gives all current courses for the current trimester
                - `!all_assignments`: Gives all unsubmitted assignments
                - `!teacher <section>`: Gives the name of the teacher for the given section
                - `!anm <section>`: Gives the latest announcement for the given section
                - `!section <subject>`: Gives the section of the given subject
                - `!due_today`: Gives all assignments currently due today'''

        await message.channel.send(msg)
# fix help message


async def listen_to_courses(message, courses, cache):
    if message.content.startswith('!courses'):
        await message.channel.typing()
        if not cache:
            all_courses = cf.get_all_course_names(courses=courses)
            for course in all_courses:
                cache.append(course)
            print('Cached Courses from courses listener')

        for course in cache:
            await message.channel.typing()
            await message.channel.send(course)

    return cache


async def listen_to_assignments(message, courses, cache):
    if message.content.startswith('!all_assignments'):
        await message.channel.typing()
        if not cache:
            cache = cf.get_all_pending_assignments(courses=courses)
            print('Cached Assignments from assignments listener')
            format_data(cache)

        await send_assignment_messages(message=message, pending_assignments=cache)

    return cache


async def listen_to_teacher(message, courses):
    if message.content.startswith('!teacher '):
        await message.channel.typing()
        course_key = message.content[9:].upper()
        teacher = cf.get_teacher(courses=courses, course_key=course_key)

        if not teacher:
            message_str = "Course Not Found"
        else:
            message_str = f"{teacher}"

        await message.channel.send(message_str)


async def listen_to_announcement(message, courses):
    if message.content.startswith('!anm '):
        await message.channel.typing()
        course_key = message.content[5:].upper()
        announcement = cf.get_announcement(courses=courses, course_key=course_key)

        if not announcement:
            message_str = "Course Not Found"
        else:
            announcement = html2text(announcement)
            message_str = f"{announcement}"

        await message.channel.send(message_str)


async def listen_to_section(message, courses):
    if message.content.startswith('!section '):
        await message.channel.typing()
        course_key = message.content[9:].upper()
        section = cf.get_section(courses=courses, course_key=course_key)

        if not section:
            message_str = "Section Not Found"
        else:
            message_str = f"{section}"

        await message.channel.send(message_str)


async def listen_to_due_today(message, pending_assignments, courses, cache):
    if message.content.startswith('!due_today'):
        await message.channel.typing()

        if not pending_assignments:
            pending_assignments = cf.get_all_pending_assignments(courses=courses)
            print("Cached Assignments from due_today listener")
            format_data(pending_assignments)

        if not cache:
            cache = cf.get_all_due_today(pending_assignments)
            print('Cached Due Today from due_today listener')
            if not cache:
                await message.channel.send('No Due Today')
                return

        for assignment in cache:
            await message.channel.typing()
            message_str = f"• {assignment['name']}"
            await message.channel.send(message_str)

    return cache


async def send_assignment_messages(message, pending_assignments):
    for course, assignments in pending_assignments.items():
        await message.channel.typing()
        for assignment_id, assignment_info in assignments.items():
            message_str = f"• {assignment_info['name']} ({course})"
            await message.channel.send(message_str)
