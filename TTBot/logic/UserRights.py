# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.logic.Environment import Environment
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.module.core.CommandCore import CommandCore
from TTBot.module.Module import Module

class UserRights(minidi.Injectable):
	pEnvironment: Environment
	pMessageEvaluator: MessageEvaluator
	pModuleManager: ModuleManager

	def allowModuleExecution(self, pModule: Module, pMessage: Message) -> bool:
		channelName = pMessage.getChannel().getName()

		isCoreCommand = isinstance(pModule, CommandCore)
		isBotChannel = self.pEnvironment.getTwitchBotUsername() == channelName
		isMainDevMessage = self.pMessageEvaluator.isMainDeveloperMessage(pMessage)
		isOwnerMessage = self.pMessageEvaluator.isOwnerMessage(pMessage)
		allowCoreCommandExecution = isBotChannel or isMainDevMessage or isOwnerMessage

		if isCoreCommand and allowCoreCommandExecution:
			return True
		
		if channelName not in self.pModuleManager.getChannels():
			raise RuntimeError(f"Cannot execute code on channel '{channelName}', did not join yet!")
		
		moduleId = pModule.getModuleId()
		minimumAccessLevel = self.pModuleManager.getMinimumAccessLevel(channelName, moduleId)
		return self.pMessageEvaluator.getUserLevel(pMessage) >= minimumAccessLevel
	# def allowModuleExecution(self, pModule: Module, pMessage: Message) -> bool
# class UserRights(minidi.Injectable)