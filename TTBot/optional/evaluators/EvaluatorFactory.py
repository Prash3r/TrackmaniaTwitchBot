# vendor
import minidi

# local
from .Evaluator import Evaluator
from .EvaluatorLuckers import EvaluatorLuckers
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class EvaluatorFactory:
	@staticmethod
	def create(evaluatorClass, pTwitchBot, ctx) -> Evaluator:
		pEvaluatorInstance = evaluatorClass()

		if isinstance(pEvaluatorInstance, EvaluatorLuckers):
			pEvaluatorInstance.pProcessVariables = minidi.get(ProcessVariables)

		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)		
		pEvaluatorInstance.message = pTwitchMessageEvaluator.getContent(ctx)
		pEvaluatorInstance.messageAuthor = pTwitchMessageEvaluator.getAuthorName(ctx)
		pEvaluatorInstance.messageChannel = pTwitchMessageEvaluator.getChannelName(ctx) # probably breaks for whispers

		return pEvaluatorInstance
	# def create(evaluatorClass, pTwitchBot, ctx) -> Evaluator
# class EvaluatorFactory