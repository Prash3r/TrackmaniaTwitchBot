# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.logic.Developers import Developers

class MessageEvaluator(minidi.Injectable):
	pDevelopers: Developers

	def getUserLevel(self, pMessage: Message) -> int:
		pAuthor = pMessage.getAuthor()

		try:
			if self.isDeveloperMessage(pMessage) or self.isOwnerMessage(pMessage):
				return 100
			elif pAuthor.isMod():
				return 10
			elif pAuthor.isSubscriber():
				return 5
			else:
				return 1
		except:
			return 1
	# def getUserLevel(self, pMessage: Message) -> int

	def isDeveloperMessage(self, pMessage: Message) -> bool:
		authorName = pMessage.getAuthor().getName()
		return authorName.lower() in self.pDevelopers.getMainDevelopers()
	# def isDeveloperMessage(self, pMessage: Message) -> bool

	def isOwnerMessage(self, pMessage: Message) -> bool:
		authorName = pMessage.getAuthor().getName()
		channelName = pMessage.getChannel().getName()
		return authorName.lower() == channelName.lower()
	# def isOwnerMessage(self, pMessage: Message) -> bool
# class MessageEvaluator(minidi.Injectable)