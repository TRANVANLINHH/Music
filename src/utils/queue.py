def queue_command(ctx):
    """Displays the current music queue."""
    if not ctx.voice_client or not ctx.voice_client.is_connected():
        return ctx.send("I'm not connected to a voice channel.")

    if not ctx.guild.music_queue or len(ctx.guild.music_queue) == 0:
        return ctx.send("The queue is currently empty.")

    queue_list = "\n".join(f"{i + 1}. {song.title}" for i, song in enumerate(ctx.guild.music_queue))
    ctx.send(f"Current queue:\n{queue_list}")
    