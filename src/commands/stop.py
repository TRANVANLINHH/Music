def stop(ctx):
    """Stops the music and clears the queue."""
    if ctx.voice_client is None:
        return await ctx.send("I'm not playing any music.")

    # Stop the music
    ctx.voice_client.stop()
    
    # Clear the queue
    if hasattr(ctx.guild, 'music_queue'):
        ctx.guild.music_queue.clear()
    
    await ctx.send("Music stopped and the queue has been cleared.")
    