def pause(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        return ctx.send("Music paused.")
    else:
        return ctx.send("No music is currently playing.")
    