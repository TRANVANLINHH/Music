def resume(ctx):
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        return "Resumed the music!"
    else:
        return "The music is not paused."
    