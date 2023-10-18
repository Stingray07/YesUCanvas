import discord
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def run_bot():
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

    bot.run(BOT_TOKEN)


async def listen_to_hello(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


async def listen_to_type(message):
    if message.content.startswith('!type'):
        await message.channel.typing()
        time.sleep(2)
        await message.channel.send('Typed')


async def listen_to_courses(message):
    if message.content.startswith('!courses'):
        await message.channel.typing()

