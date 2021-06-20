# pylib
import re

# vendor
import minidi

# local
from .Evaluator import Evaluator
from .EvaluatorLuckers import EvaluatorLuckers
from .EvaluatorOoga import EvaluatorOoga
from .EvaluatorPing import EvaluatorPing
from TTBot.logic.Logger import Logger
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.logic.UserRights import UserRights

class EvaluatorRunner(minidi.Injectable):
	EVALUATORS = [
		EvaluatorLuckers,
		EvaluatorOoga,
		EvaluatorPing
	]

	pLogger: Logger
	pTwitchMessageEvaluator: TwitchMessageEvaluator
	pUserRights: UserRights

	async def _checkExecutionSingle(self, pEvaluator: Evaluator, pMessage):
		messageContent = self.pTwitchMessageEvaluator.getContent(pMessage)

		if not re.search(pEvaluator.getMessageRegex(), messageContent.lower()):
			return
		
		if self.pUserRights.allowModuleExecution(pEvaluator, pMessage):
			await self._executeSingle(pEvaluator, pMessage)
	# async def _checkExecutionSingle(self, pEvaluator: Evaluator, pMessage)

	async def _executeSingle(self, pEvaluator: Evaluator, pMessage):
		try:
			result = await pEvaluator.execute(pMessage)
			pChannel = self.pTwitchMessageEvaluator.getChannel(pMessage)
			await pChannel.send(result)
			self.pLogger.info(f"{pEvaluator.__class__.__name__} did trigger")
		except Exception as e:
			self.pLogger.exception(e)
	# async def _executeSingle(self, pEvaluator: Evaluator, pMessage)

	async def execute(self, pMessage):
		for evaluatorClass in self.EVALUATORS:
			await self._checkExecutionSingle(minidi.get(evaluatorClass), pMessage)
	# async def execute(self, pMessage)
# class EvaluatorRunner