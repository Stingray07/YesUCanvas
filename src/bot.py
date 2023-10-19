import discord
import os
import time
from canvas import get_current_courses, format_data
import course_functions as cf
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def run_bot():
    print("REQUESTING COURSES FROM CANVAS API...")
    courses = get_current_courses()
    format_data(courses)
    BOT_TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        await listen_to_hello(message)
        await listen_to_type(message)
        await listen_to_courses(message=message, courses=courses)
        await listen_to_assignments(message=message, courses=courses)

    bot.run(BOT_TOKEN)


async def listen_to_hello(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


async def listen_to_type(message):
    if message.content.startswith('!type'):
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send('Typed')


async def listen_to_courses(message, courses):
    if message.content.startswith('!courses'):
        await message.channel.typing()
        names = cf.get_all_course_names(courses=courses)
        for name in names:
            await message.channel.typing()
            await message.channel.send(name)


async def listen_to_assignments(message, courses):
    if message.content.startswith('!all_assignments'):
        await message.channel.typing()
        pending_assignments = cf.get_all_pending_assignments(courses=courses)
        format_data(pending_assignments)
        for course, assignments in pending_assignments.items():
            await message.channel.typing()
            for assignment_id, value in assignments.items():
                await message.channel.send(f"• {pending_assignments[course][assignment_id]['name']} ({course})")

