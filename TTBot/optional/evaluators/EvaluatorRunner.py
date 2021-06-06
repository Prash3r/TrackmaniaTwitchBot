# pylib
import logging
import re

# vendor
from TTBot import _tools

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
		for evaluatorClass in self.EVALUATORS:
			if not re.search(evaluatorClass.getMessageRegex(), ctx.content.lower()):
				continue
			
			if _tools.rights(pTwitchBot, ctx, evaluatorClass.getRightsId()):
				pEvaluatorInstance = EvaluatorFactory.create(evaluatorClass, pTwitchBot, ctx)
				try:
					result = await pEvaluatorInstance.execute()
					await ctx.channel.send(result)
					logging.info(f"{evaluatorClass.__name__} did trigger")
				except Exception as e:
					logging.exception(e)
			# if _tools.rights(pTwitchBot, ctx, evaluatorClass.getRightsId())
		# for evaluatorClass in self.EVALUATORS
	# def execute(self, ctx)
# class EvaluatorRunner