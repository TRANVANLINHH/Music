from discord.ext import commands
import youtube_dl

class PlayCommand:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def play(self, ctx, *, url):
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'type': 'audio/ffmpeg',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url = info['formats'][0]['url']
            title = info['title']

        ctx.voice_client.play(discord.FFmpegPCMAudio(url))
        await ctx.send(f'Now playing: {title}')

def setup(bot):
    bot.add_cog(PlayCommand(bot))
    