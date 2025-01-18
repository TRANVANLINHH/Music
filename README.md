# Discord Music Bot

This project is a Discord music bot built using Python. It allows users to play music from YouTube, manage a music queue, and control playback through various commands.

## Features


- Play music from YouTube
- Manage a music queue
- Control playback (play, skip, stop, pause, resume)
- Adjust volume
- Display current song information
- Search for songs
- Loop and shuffle the playlist
- Help command for user assistance

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-music-bot.git
   cd discord-music-bot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the bot:
   ```
   python src/bot.py
   ```

2. Use the following commands in your Discord server:

   - `!play <song>`: Play a song or add it to the queue.
   - `!skip`: Skip the currently playing song.
   - `!stop`: Stop the music and clear the queue.
   - `!queue`: Display the current playlist.
   - `!clear`: Clear the music queue.
   - `!volume <level>`: Change the playback volume.
   - `!now`: Display information about the currently playing song.
   - `!search <song>`: Search for a song.
   - `!pause`: Pause the currently playing song.
   - `!resume`: Resume playback of a paused song.
   - `!next`: Play the next song in the queue.
   - `!loop`: Toggle the repeat mode for the current song.
   - `!shuffle`: Shuffle the current playlist.
   - `!help`: Display all available commands.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.