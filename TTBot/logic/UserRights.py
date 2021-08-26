# vendor
import minidi

# local
from .MariaDbWrapper import MariaDbWrapper
from .TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.optional.commands.CommandCore import CommandCore
from TTBot.optional.Module import Module

class UserRights(minidi.Injectable):
	pMariaDbWrapper: MariaDbWrapper
	pTwitchMessageEvaluator: TwitchMessageEvaluator

	def allowModuleExecution(self, pModule: Module, pMessage) -> bool:
		isCoreCommand = isinstance(pModule, CommandCore)
		isOwnerMessage = self.pTwitchMessageEvaluator.isOwnerMessage(pMessage)
		isBotChannel = self.pTwitchMessageEvaluator.isBotChannel(pMessage)

		if isCoreCommand and (isOwnerMessage or isBotChannel):
			return True
		
		channelName = self.pTwitchMessageEvaluator.getChannelName(pMessage)
		rightsId = pModule.getRightsId()

		try:
			rows = self.pMariaDbWrapper.fetch(f"SELECT {rightsId} FROM modules WHERE channel = '{channelName.lower()}' LIMIT 1;")
		except:
			return False
		
		if not rows:
			return False
		
		minimumAccessLevel = rows[0][rightsId]
		if minimumAccessLevel in [0, None]:
			return False

		return self.pTwitchMessageEvaluator.getUserLevel(pMessage) >= minimumAccessLevel
	# def allowModuleExecution(self, pModule: Module, pMessage) -> bool
# class UserRights(minidi.Injectable)