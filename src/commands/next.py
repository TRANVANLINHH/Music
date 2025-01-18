def next_song(ctx):
    # Get the current queue from the context
    queue = ctx.bot.queue

    # Check if there are songs in the queue
    if len(queue) > 0:
        # Remove the first song from the queue and play it
        next_song = queue.pop(0)
        ctx.voice_client.play(next_song)
        await ctx.send(f'Now playing: {next_song.title}')
    else:
        await ctx.send('No more songs in the queue.')
        