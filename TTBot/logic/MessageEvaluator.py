# vendor
import minidi

# local
from TTBot.data.Message import Message

class MessageEvaluator(minidi.Injectable):
	def getUserLevel(self, pMessage: Message) -> int:
		pAuthor = pMessage.getAuthor()
		authorName = pAuthor.getName()

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
		authorName = pMessage.getAuthor().getName()
		channelName = pMessage.getChannel().getName()
		return authorName.lower() == channelName.lower()
	# def isOwnerMessage(self, pMessage: Message) -> bool
# class MessageEvaluator(minidi.Injectable)