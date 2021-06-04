from twitchio.ext import commands
import random
import logging

@commands.command(name='roll')
async def CMD_roll(self, ctx, args):
    if not self.rights(ctx, 'roll'):
        # maybe whisper that invoking person has no rights
        return
    logging.info(f"Command '!roll' running in channel '{ctx.channel.name}' invoked by user '{ctx.author.name}'")
    try:
        number = int(args)
        result = random.randint(1,number)
        if result == 69 :
            await ctx.channel.send(f'{result}/{number} - NICE')
        elif number == 420 :
            await ctx.channel.send(f'No, @{ctx.author.name} - we do not support drugs in this chat ({result}/{number})')
        else:
            await ctx.channel.send(f'{result}/{number}')
    except:
        pass