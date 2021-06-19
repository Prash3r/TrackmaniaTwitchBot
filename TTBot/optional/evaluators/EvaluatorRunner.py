# pylib
import re

# vendor
import minidi
from TTBot import _tools
from TTBot.logic.Logger import Logger
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

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

		for evaluatorClass in self.EVALUATORS:
			if not re.search(evaluatorClass.getMessageRegex(), ctx.content.lower()):
				continue
			
			if _tools.rights(pTwitchBot, ctx, evaluatorClass.getRightsId()):
				pEvaluatorInstance = EvaluatorFactory.create(evaluatorClass, pTwitchBot, ctx)
				try:
					result = await pEvaluatorInstance.execute()
					await pChannel.send(result)
					pLogger.info(f"{evaluatorClass.__name__} did trigger")
				except Exception as e:
					pLogger.exception(e)
			# if _tools.rights(pTwitchBot, ctx, evaluatorClass.getRightsId())
		# for evaluatorClass in self.EVALUATORS
	# def execute(self, ctx)
# class EvaluatorRunner