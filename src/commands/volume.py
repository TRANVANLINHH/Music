def set_volume(ctx, volume: int):
    """Set the volume for the music player."""
    if 0 <= volume <= 100:
        # Assuming `player` is your music player instance
        player.volume = volume
        await ctx.send(f"Volume set to {volume}%.")
    else:
        await ctx.send("Volume must be between 0 and 100.")

async def volume_command(ctx, volume: int):
    """Command to change the volume."""
    await set_volume(ctx, volume)
    