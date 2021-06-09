from TTBot.optional.evaluators.EvaluatorRunner import EvaluatorRunner
from TTBot.optional.commands.CommandRunner import CommandRunner
import logging
from twitchio.ext import commands

pEvaluatorRunner = EvaluatorRunner()
pCommandRunner = CommandRunner()

async def handle(self, ctx):
    # This function is called by every message in chat and handles commands and evaluations accordingly
    logging.debug(f"{ctx.author.name}\t:{ctx.content}")
    try:
        # handle commands
        await self.handle_commands(ctx) # twitchio function that will call the decorated functions for example in TTBot/optional/commands
        # CORE COMMANDS are still running via the decorators provided by twitchio
    except commands.errors.CommandNotFound:
        # no message because this would spam the log with commands meant for other bots
        pass
    await pCommandRunner.execute(self, ctx)
    await pEvaluatorRunner.execute(self, ctx)
# async def handle(self, ctx)