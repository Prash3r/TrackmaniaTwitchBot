# local
from .Evaluator import Evaluator
from .EvaluatorLuckers import EvaluatorLuckers

class EvaluatorFactory:
	@staticmethod
	def create(evaluatorClass, pTwitchBot, ctx) -> Evaluator:
		pEvaluatorInstance = evaluatorClass()

		if isinstance(pEvaluatorInstance, EvaluatorLuckers):
			pEvaluatorInstance.funcGetPV = pTwitchBot.DB_GetPV
			pEvaluatorInstance.funcWritePV = pTwitchBot.DB_WritePV
			pEvaluatorInstance.messageAuthor = ctx.author.name
		# if isinstance(pEvaluatorInstance, EvaluatorLuckers)

		return pEvaluatorInstance
	# def create(evaluatorClass, pTwitchBot, ctx) -> Evaluator
# class EvaluatorFactory