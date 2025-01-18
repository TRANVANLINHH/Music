from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='DISCORD_BOT_PREFIX')

# Load commands from the commands directory
for filename in os.listdir('./src/commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Run the bot with the specified token
if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN')
    bot.run(token)
    