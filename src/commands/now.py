def now(ctx):
    # Assuming you have a way to access the currently playing song
    current_song = get_current_song()  # This function should be defined elsewhere in your code

    if current_song:
        title = current_song['title']
        artist = current_song['artist']
        duration = current_song['duration']
        await ctx.send(f"Now playing: **{title}** by **{artist}** | Duration: **{duration}**")
    else:
        await ctx.send("No song is currently playing.")
        