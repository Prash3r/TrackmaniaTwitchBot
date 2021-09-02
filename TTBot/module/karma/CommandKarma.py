# local
from TTBot.data.Message import Message
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.module.Command import Command

class CommandKarma(Command):
	pInputSanitizer: InputSanitizer
	pLocalVariables: LocalVariables
	pMessageEvaluator: MessageEvaluator

	def getCommandTrigger(self):
		return 'karma'
	
	def getModuleId(self) -> str:
		return 'karma'
	
	async def execute(self, pMessage: Message, args: list) -> str:
		channelName = pMessage.getChannel().getName()

		isAtleastModMessage = self.pMessageEvaluator.isAtleastModMessage(pMessage)
		newKarma = int(args[0]) if len(args) >= 1 and self.pInputSanitizer.isInteger(args[0]) else None

		if isAtleastModMessage and (newKarma is not None):
			self.pLocalVariables.write('karma', channelName, newKarma)
			return f"Successfully changed karma, current streamer karma: {newKarma}"
		# if isAtleastModMessage and (newKarma is not None)
		
		karma = self.pLocalVariables.get('karma', channelName, 0)
		return f"Current streamer karma: {karma}"
	# async def execute(self, pMessage: Message, args: list) -> str
# class CommandKarma(Command)