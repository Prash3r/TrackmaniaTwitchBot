from TTBot.optional.evaluators.EvaluatorRunner import EvaluatorRunner
# vendor
import minidi

# local
from .logic.Logger import Logger
from .logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from .optional.commands.CommandRunner import CommandRunner
from .optional.evaluators.EvaluatorRunner import EvaluatorRunner

async def handle(self, ctx):
    # This function is called by every message in chat and handles commands and evaluations accordingly
    pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
    pLogger: Logger = minidi.get(Logger)
    pLogger.debug(f"{pTwitchMessageEvaluator.getAuthorName(ctx)}\t:{pTwitchMessageEvaluator.getContent(ctx)}")

    pCommandRunner: CommandRunner = minidi.get(CommandRunner)
    await pCommandRunner.execute(ctx)

    pEvaluatorRunner: EvaluatorRunner = minidi.get(EvaluatorRunner)
    await pEvaluatorRunner.execute(ctx)
# async def handle(self, ctx)