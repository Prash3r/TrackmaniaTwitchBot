from twitchio.ext import commands
import random
import time
import logging


@commands.command(name='joke')
async def CMD_joke(self, ctx):
    if not self.rights(ctx, 'joke'):
        # maybe whisper that invoking person has no rights
        return
    logging.info(f"Command '!joke' running in channel '{ctx.channel.name}' invoked by user '{ctx.author.name}'")
    if ctx.author.name == "Fegir":
        await ctx.channel.send('kem1W')
    if ctx.author.name == "AmaterasuTM":
        if random.choice([True, False, False, False, False, False, False]):
            await ctx.channel.send('kem1W')
        else:
            await ctx.channel.send('you know who!')
    else:
        if random.choice([True, False, False, False, False, False, False]):
            await ctx.channel.send('modCheck')
            time.sleep(1)
            await ctx.channel.send('Fegir')
            time.sleep(2)
            await ctx.channel.send('KEKW')
        else:
            await ctx.channel.send('Fegir')