# pylib
import re

# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.logic.Logger import Logger
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.logic.UserRights import UserRights
from TTBot.module.Evaluator import Evaluator
from TTBot.module.ModuleList import ModuleList

class EvaluatorRunner(minidi.Injectable):
	pLogger: Logger
	pModuleFactory: ModuleFactory
	pModuleList: ModuleList
	pUserRights: UserRights

	async def _checkExecutionSingle(self, pEvaluator: Evaluator, pMessage: Message):
		messageContent = pMessage.getContent()

		if not re.search(pEvaluator.getMessageRegex(), messageContent.lower()):
			return
		
		if self.pUserRights.allowModuleExecution(pEvaluator, pMessage):
			await self._executeSingle(pEvaluator, pMessage)
	# async def _checkExecutionSingle(self, pEvaluator: Evaluator, pMessage: Message)

	async def _executeSingle(self, pEvaluator: Evaluator, pMessage: Message):
		try:
			result = await pEvaluator.execute(pMessage)
			pChannel = pMessage.getChannel()
			await pChannel.sendMessage(result)
			self.pLogger.info(f"{pEvaluator.__class__.__name__} did trigger")
		except Exception as e:
			self.pLogger.exception(e)
	# async def _executeSingle(self, pEvaluator: Evaluator, pMessage: Message)

	async def execute(self, pMessage: Message):
		evaluatorClasses = self.pModuleList.getEvaluatorClasses()

		for evaluatorClass in evaluatorClasses:
			pEvaluatorClassInstance = self.pModuleFactory.createEvaluator(evaluatorClass)
			await self._checkExecutionSingle(pEvaluatorClassInstance, pMessage)
		# for evaluatorClass in evaluatorClasses
	# async def execute(self, pMessage: Message)
# class EvaluatorRunner