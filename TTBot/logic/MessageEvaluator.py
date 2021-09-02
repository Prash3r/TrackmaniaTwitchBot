# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.logic.Developers import Developers
from TTBot.logic.UserLevel import UserLevel

class MessageEvaluator(minidi.Injectable):
	pDevelopers: Developers

	def getUserLevel(self, pMessage: Message) -> int:
		pAuthor = pMessage.getAuthor()

		if self.isMainDeveloperMessage(pMessage) or self.isOwnerMessage(pMessage):
			return UserLevel.ADMIN
		elif pAuthor.isMod():
			return UserLevel.MOD
		elif pAuthor.isSubscriber():
			return UserLevel.SUB
		else:
			return UserLevel.USER
	# def getUserLevel(self, pMessage: Message) -> int

	def isAtleastModMessage(self, pMessage: Message) -> bool:
		return self.getUserLevel(pMessage) >= UserLevel.MOD
	# def isAtleastModMessage(self, pMessage: Message) -> bool

	def isMainDeveloperMessage(self, pMessage: Message) -> bool:
		authorName = pMessage.getAuthor().getName()
		return authorName.lower() in self.pDevelopers.getMainDevelopers()
	# def isMainDeveloperMessage(self, pMessage: Message) -> bool

	def isOwnerMessage(self, pMessage: Message) -> bool:
		authorName = pMessage.getAuthor().getName()
		channelName = pMessage.getChannel().getName()
		return authorName.lower() == channelName.lower()
	# def isOwnerMessage(self, pMessage: Message) -> bool
# class MessageEvaluator(minidi.Injectable)