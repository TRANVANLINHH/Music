from discord.ext import commands
from utils.youtube import search_youtube

class SearchCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search')
    async def search(self, ctx, *, query: str):
        results = search_youtube(query)
        if results:
            response = "\n".join([f"{index + 1}. {result['title']} - {result['url']}" for index, result in enumerate(results)])
            await ctx.send(f"**Search Results:**\n{response}")
        else:
            await ctx.send("No results found.")

def setup(bot):
    bot.add_cog(SearchCommand(bot))
    