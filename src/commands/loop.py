def toggle_loop(ctx):
    """Toggle the loop mode for the current song."""
    if ctx.guild.id not in ctx.bot.looping:
        ctx.bot.looping[ctx.guild.id] = True
        await ctx.send("Loop mode is now enabled.")
    else:
        ctx.bot.looping[ctx.guild.id] = False
        await ctx.send("Loop mode is now disabled.")
        