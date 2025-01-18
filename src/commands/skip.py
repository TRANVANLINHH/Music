def skip(ctx):
    """Skip the currently playing song."""
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Skipped the current song.")
    else:
        await ctx.send("No song is currently playing.")
        