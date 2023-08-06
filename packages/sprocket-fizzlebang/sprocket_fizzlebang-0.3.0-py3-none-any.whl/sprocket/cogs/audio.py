import discord.utils
from discord.ext import commands

from sprocket.util.common import repo_root
from sprocket.util.common import find_audio
from sprocket.util.common import ls


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guild = ""

    def is_connected(self, ctx):
        voice_client = discord.utils.get(
            self.bot.voice_clients, guild=self.guild
        )

        return voice_client and voice_client.is_connected()

    @commands.command(name="join", hidden=True)
    @commands.is_owner()
    async def join(self, ctx):
        self.guild = ctx.guild

        channel = ctx.message.author.voice.channel
        if not self.is_connected(ctx):
            await channel.connect()

    @commands.command(name="leave", hidden=True)
    @commands.is_owner()
    async def leave(self, ctx):
        if self.is_connected(ctx):
            await ctx.voice_client.disconnect()

    @commands.command(name="play")
    async def play(self, ctx, *args):
        if self.is_connected(ctx):

            voice_client: discord.VoiceClient = discord.utils.get(
                self.bot.voice_clients, guild=self.guild
            )

            search_result = find_audio(args[0])

            if type(search_result) == str:
                audio_source = discord.FFmpegPCMAudio(search_result)
                if not voice_client.is_playing():
                    voice_client.play(audio_source, after=None)

            elif type(search_result) == list:
                possible_matches = "\n".join(search_result)
                msg = "```fix\nDid you mean one of these?:\n{}```".format(
                    possible_matches
                )
                await ctx.send(msg)

    @commands.command(name="stop")
    async def stop(self, ctx):
        if self.is_connected(ctx):
            voice_client: discord.VoiceClient = discord.utils.get(
                self.bot.voice_clients, guild=self.guild
            )
            if voice_client.is_playing():
                voice_client.stop()

    @commands.command(name="pause")
    async def pause(self, ctx):
        if self.is_connected(ctx):
            voice_client: discord.VoiceClient = discord.utils.get(
                self.bot.voice_clients, guild=self.guild
            )
            if voice_client.is_playing():
                voice_client.pause()
            elif voice_client.is_paused():
                voice_client.resume()

    @commands.command(name="sounds")
    async def sounds_list(self, ctx):
        user = await self.bot.fetch_user(ctx.message.author.id)

        file_list = " ".join(ls(repo_root("data", "audio"), delim="."))

        # paginate file_list
        while len(file_list) > 2000:
            split = 1900
            while file_list[split] != " ":
                split += 1
            msg = "```fix\nSounds:\n--------\n{}```".format(file_list[:split])
            await user.send(msg)
            file_list = file_list[split:]

        msg = "```fix\nSounds:\n--------\n{}```".format(file_list)
        await user.send(msg)


def setup(bot):
    bot.add_cog(Audio(bot))
