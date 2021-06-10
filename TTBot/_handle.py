from TTBot.optional.evaluators.EvaluatorRunner import EvaluatorRunner
# vendor
import minidi
from .logic.Logger import Logger

# local
from .optional.commands.CommandRunner import CommandRunner
from .optional.evaluators.EvaluatorRunner import EvaluatorRunner

pEvaluatorRunner = EvaluatorRunner()
pCommandRunner = CommandRunner()

async def handle(self, ctx):
    # This function is called by every message in chat and handles commands and evaluations accordingly
    pLogger: Logger = minidi.get(Logger)
    pLogger.debug(f"{ctx.author.name}\t:{ctx.content}")

    await pCommandRunner.execute(self, ctx)
    await pEvaluatorRunner.execute(self, ctx)
# async def handle(self, ctx)