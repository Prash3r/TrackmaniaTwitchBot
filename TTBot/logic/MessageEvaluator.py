# pylib
from abc import abstractmethod

# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel

class MessageEvaluator(minidi.Injectable):
	def getAuthor(self, pMessage: Message) -> MessageAuthor:
		return pMessage.getAuthor()

	def getAuthorName(self, pMessage: Message) -> str:
		return pMessage.getAuthor().getName()

	def getChannel(self, pMessage: Message) -> MessageChannel:
		return pMessage.getChannel()

	def getChannelName(self, pMessage: Message) -> str:
		return pMessage.getChannel().getName()

	def getContent(self, pMessage: Message) -> str:
		return pMessage.getContent()

	def getUserLevel(self, pMessage: Message) -> int:
		pAuthor = self.getAuthor(pMessage)
		authorName = self.getAuthorName(pMessage)

		try:
			if authorName.lower() == 'prash3r' or self.isOwnerMessage(pMessage):
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

	def isOwnerMessage(self, pMessage: Message) -> bool:
		authorName = self.getAuthorName(pMessage)
		channelName = self.getChannelName(pMessage)
		return authorName.lower() == channelName.lower()
	# def isOwnerMessage(self, pMessage: Message) -> bool
# class MessageEvaluator(minidi.Injectable)