from discord.ext import commands
import random

class ShuffleCommand:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shuffle')
    async def shuffle(self, ctx):
        if not ctx.voice_client or not ctx.voice_client.is_connected():
            await ctx.send("I'm not connected to a voice channel.")
            return

        if not self.bot.queue:
            await ctx.send("The queue is currently empty.")
            return

        random.shuffle(self.bot.queue)
        await ctx.send("The queue has been shuffled.")

def setup(bot):
    bot.add_cog(ShuffleCommand(bot))
    