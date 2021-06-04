from twitchio.ext import commands
import random
import logging
      
@commands.command(name='score')
async def CMD_score(self, ctx):
    if not self.rights(ctx, 'score'):
        # maybe whisper that invoking person has no rights
        return
    logging.info(f"Command '!score' running in channel '{ctx.channel.name}' invoked by user '{ctx.author.name}'")
    result = random.randint(0,100000)
    if result == 69:
        await ctx.channel.send(f'{result} - NICE')
    if result == 69420:
        await ctx.channel.send(f'{result} - MEGANICE')
    elif ('69' in str(result)):
        await ctx.channel.send(f'{result} - partly nice')
    else:
        await ctx.channel.send(f'{result}')