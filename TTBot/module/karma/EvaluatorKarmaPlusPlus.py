# local
from TTBot.data.Message import Message
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.module.Evaluator import Evaluator

class EvaluatorKarmaPlusPlus(Evaluator):
	pLocalVariables: LocalVariables

	def getMessageRegex(self) -> str:
		return r'(^\+\+$)|(^\+\+ .*$)|(^.* \+\+$)'
	
	def getModuleId(self) -> str:
		return 'karma'
	
	async def execute(self, pMessage: Message) -> str:
		pChannel = pMessage.getChannel()
		channelName = pChannel.getName()

		currentKarma = self.pLocalVariables.get('karma', channelName, 0)
		newKarma = currentKarma + 1
		self.pLocalVariables.write('karma', channelName, newKarma)

		return f"Successfully voted ++, current streamer karma: {newKarma}"
	# async def execute(self, pMessage: Message) -> str
# class EvaluatorKarmaPlusPlus(Evaluator)