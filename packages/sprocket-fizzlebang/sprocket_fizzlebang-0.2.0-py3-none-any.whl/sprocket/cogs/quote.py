from discord.ext import commands
from sprocket.data.loader import Loader
import random


class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.files = ["13th-warrior.txt", "lotr.txt", "baldursgate.txt"]
        self.Loader = Loader()
        self.quotes = []
        self.read_files()

    @commands.command(name="speak", aliases=["say", "s"])
    async def speak(self, ctx):
        quote = random.choice(self.quotes)
        await ctx.send("```fix\n{0}```".format(quote))

    def read_files(self):
        for file in self.files:
            self.Loader.load(file)
            if self.Loader:
                strings = self.Loader.raw.split("\n\n")
                self.quotes += strings


def setup(bot):
    bot.add_cog(Quote(bot))
