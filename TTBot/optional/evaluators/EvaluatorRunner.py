# pylib
import re

# vendor
import minidi
from TTBot.logic.Logger import Logger
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.logic.UserRights import UserRights

# local
from .EvaluatorFactory import EvaluatorFactory
from .EvaluatorLuckers import EvaluatorLuckers
from .EvaluatorOoga import EvaluatorOoga
from .EvaluatorPing import EvaluatorPing

class EvaluatorRunner:
	EVALUATORS = [
		EvaluatorLuckers,
		EvaluatorOoga,
		EvaluatorPing
	]

	async def execute(self, pTwitchBot, ctx) -> bool:
		pLogger = minidi.get(Logger)
		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
		pChannel = pTwitchMessageEvaluator.getChannel(ctx)
		pUserRights: UserRights = minidi.get(UserRights)

		for evaluatorClass in self.EVALUATORS:
			if not re.search(evaluatorClass.getMessageRegex(), ctx.content.lower()):
				continue
			
			if pUserRights.allowModuleExecution(ctx, evaluatorClass):
				pEvaluatorInstance = EvaluatorFactory.create(evaluatorClass, pTwitchBot, ctx)
				try:
					result = await pEvaluatorInstance.execute()
					await pChannel.send(result)
					pLogger.info(f"{evaluatorClass.__name__} did trigger")
				except Exception as e:
					pLogger.exception(e)
			# if pUserRights.allowModuleExecution(ctx, evaluatorClass)
		# for evaluatorClass in self.EVALUATORS
	# def execute(self, ctx)
# class EvaluatorRunner