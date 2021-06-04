from twitchio.ext import commands
import logging

@commands.command(name='kem')
async def CMD_kem(self, ctx, args=""):
    if not self.rights(ctx, 'kem'):
        # maybe whisper that invoking person has no rights
        return
    logging.info(f"Command '!kem' running in channel '{ctx.channel.name}' invoked by user '{ctx.author.name}'")
    reply = 'kem1W'
    try:
        number = int(args[0])
        if number > 10:
            number = 10
        while (number > 1):
            number = number - 1
            reply = reply + ' kem1W'
    except:
        reply = 'kem1W'
    await ctx.channel.send(reply)