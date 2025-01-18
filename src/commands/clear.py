def clear_queue(ctx):
    """Clears the music queue."""
    if ctx.voice_client and ctx.voice_client.is_connected():
        ctx.voice_client.queue.clear()
        await ctx.send("The music queue has been cleared.")
    else:
        await ctx.send("I'm not connected to a voice channel.")
        