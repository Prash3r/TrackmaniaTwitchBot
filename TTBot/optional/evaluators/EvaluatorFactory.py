# vendor
import minidi
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

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
		# if isinstance(pEvaluatorInstance, EvaluatorLuckers)

		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)		
		pEvaluatorInstance.message = pTwitchMessageEvaluator.getContent(ctx)
		pEvaluatorInstance.messageAuthor = pTwitchMessageEvaluator.getAuthorName(ctx)
		pEvaluatorInstance.messageChannel = pTwitchMessageEvaluator.getChannelName(ctx) # probably breaks for whispers

		return pEvaluatorInstance
	# def create(evaluatorClass, pTwitchBot, ctx) -> Evaluator
# class EvaluatorFactory