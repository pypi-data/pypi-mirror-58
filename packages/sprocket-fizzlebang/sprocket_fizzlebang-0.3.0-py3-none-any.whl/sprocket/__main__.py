import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
PREFIX = ("?", "!")
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
initial_extensions = ["cogs.base", "cogs.dice", "cogs.quote", "cogs.audio"]


def get_prefix(bot, message):
    prefixes = ["?", "!"]

    return commands.when_mentioned_or(*prefixes)(bot, message)


def run():
    bot = commands.Bot(command_prefix=get_prefix, description="Erky")

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except commands.errors.ExtensionNotFound:
            bot.load_extension("sprocket." + extension)

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game(name="with himself"))
        print("Logged in as")
        print(bot.user.name)
        print(bot.user.id)
        print("------")

    bot.run(TOKEN, bot=True, reconnect=True)


if __name__ == "__main__":
    run()
