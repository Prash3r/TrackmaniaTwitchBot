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

	@abstractmethod
	def getUserLevel(self, pMessage: Message) -> int:
		pass
	
	@abstractmethod
	def isBotAuthorOfMessage(self, pMessage: Message) -> bool:
		pass

	@abstractmethod
	def isBotChannel(self, pMessage: Message) -> bool:
		pass

	def isOwnerMessage(self, pMessage: Message) -> bool:
		authorName = self.getAuthorName(pMessage)
		channelName = self.getChannelName(pMessage)
		return authorName.lower() == channelName.lower()
	# def isOwnerMessage(self, pMessage: Message) -> bool
# class MessageEvaluator(minidi.Injectable)