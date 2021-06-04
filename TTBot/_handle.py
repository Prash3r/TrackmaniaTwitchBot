import logging
import re
from twitchio.ext import commands

async def handle(self, ctx):
    # This function is called by every message in chat and handles commands and evaluations accordingly
    logging.debug(f"{ctx.author.name}\t:{ctx.content}")
    try:
        # handle commands
        await self.handle_commands(ctx) # twitchio function that will call the decorated functions for example in TTBot/optional/commands
    except commands.errors.CommandNotFound:
        # no message because this would spam the log with commands meant for other bots
        pass
    # ToDo: here i should rather handle everything via events.
    # for now i just call every evaluator and stop on the first that triggers - also means tzhis needs to be adjusted for every addition
    done = False
    if (self.rights(ctx, 'luckerscounter') and not (done)):
        done = await self.EVAL_luckerscounter(ctx)
    if (self.rights(ctx, 'ooga') and not (done)):
        done = await self.EVAL_ooga(ctx)
    if (self.rights(ctx, 'ping') and not (done)):
        done = await self.EVAL_ping(ctx)