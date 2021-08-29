# vendor
import minidi

# local
from .DbConnector import DbConnector
from .Environment import Environment
from .MessageEvaluator import MessageEvaluator
from TTBot.optional.commands.core.CommandCore import CommandCore
from TTBot.optional.Module import Module

class UserRights(minidi.Injectable):
	pDbConnector: DbConnector
	pEnvironment: Environment
	pMessageEvaluator: MessageEvaluator

	def allowModuleExecution(self, pModule: Module, pMessage) -> bool:
		channelName = pMessage.getChannel().getName().lower()

		isCoreCommand = isinstance(pModule, CommandCore)
		isOwnerMessage = self.pMessageEvaluator.isOwnerMessage(pMessage)
		isBotChannel = self.pEnvironment.getTwitchBotUsername() == channelName

		if isCoreCommand and (isOwnerMessage or isBotChannel):
			return True
		
		rightsId = pModule.getModuleId()

		rows = self.pDbConnector.fetch(f"SELECT `{rightsId}` FROM `modules` WHERE `channel` = '{channelName}' LIMIT 1;")		
		if not rows:
			return False
		
		minimumAccessLevel = rows[0][rightsId]
		if minimumAccessLevel in [0, None]:
			return False

		return self.pMessageEvaluator.getUserLevel(pMessage) >= minimumAccessLevel
	# def allowModuleExecution(self, pModule: Module, pMessage) -> bool
# class UserRights(minidi.Injectable)