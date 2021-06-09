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
		pEvaluatorInstance.message = ctx.content
		pEvaluatorInstance.messageAuthor = ctx.author.name
		pEvaluatorInstance.messageChannel = ctx.channel.name # probably breaks for whispers
		# if isinstance(pEvaluatorInstance, EvaluatorLuckers)

		return pEvaluatorInstance
	# def create(evaluatorClass, pTwitchBot, ctx) -> Evaluator
# class EvaluatorFactory