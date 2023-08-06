import os
import random

from discord.ext import commands

from sprocket.util.common import repo_root
from sprocket.util.common import ls


class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.quotes = []
        self.read_files()

    @commands.command(name="speak", aliases=["say", "s"])
    async def speak(self, ctx):
        quote = random.choice(self.quotes)
        await ctx.send("```fix\n{0}```".format(quote))

    def read_files(self):
        directory = repo_root("data", "text")
        files = ls(directory, filter="txt")
        for file in files:
            txt = open(os.path.join(directory, file), "r").read()
            strings = txt.split("\n\n")
            self.quotes += strings


def setup(bot):
    bot.add_cog(Quote(bot))
