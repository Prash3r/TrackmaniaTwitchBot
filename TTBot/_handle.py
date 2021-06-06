from TTBot.optional.evaluators.EvaluatorRunner import EvaluatorRunner
import logging
import re
from twitchio.ext import commands

pEvaluatorRunner = EvaluatorRunner()

async def handle(self, ctx):
    # This function is called by every message in chat and handles commands and evaluations accordingly
    logging.debug(f"{ctx.author.name}\t:{ctx.content}")
    try:
        # handle commands
        await self.handle_commands(ctx) # twitchio function that will call the decorated functions for example in TTBot/optional/commands
    except commands.errors.CommandNotFound:
        # no message because this would spam the log with commands meant for other bots
        pass

    await pEvaluatorRunner.execute(self, ctx)
# async def handle(self, ctx)