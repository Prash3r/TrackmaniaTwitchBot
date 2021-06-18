# vendor
import minidi
import twitchio

# local
from .Environment import Environment

class TwitchMessageEvaluator(minidi.Injectable):
	pEnvironment: Environment

	def getAuthor(self, pMessage: twitchio.Message) -> twitchio.Chatter:
		return pMessage.author

	def getChannel(self, pMessage: twitchio.Message) -> twitchio.Channel:
		return pMessage.channel

	def getUserLevel(self, pMessage: twitchio.Message) -> int:
		pAuthor = self.getAuthor(pMessage)

		try:
			if pAuthor.name.lower() == 'prash3r' or self.isOwnerMessage(pMessage):
				return 100
			elif pAuthor.is_mod():
				return 10
			elif pAuthor.is_subscriber():
				return 5
			else:
				return 1
		except:
			return 1
	# def getUserLevel(self, pMessage: twitchio.Message) -> int

	def isOwnerMessage(self, pMessage: twitchio.Message) -> bool:
		pAuthor = self.getAuthor(pMessage)
		pChannel = self.getChannel(pMessage)

		try:
			return pAuthor.name.lower() == pChannel.name.lower()
		except:
			return False
	# def isOwnerMessage(self, pMessage: twitchio.Message) -> bool

	def isBotChatHome(self, pMessage: twitchio.Message) -> bool:
		pChannel = self.getChannel(pMessage)

		try:
			return self.pEnvironment.getTwitchBotUsername() == pChannel.name.lower()
		except:
			return False
	# def isBotChatHome(self, pMessage: twitchio.Message) -> bool
# class TwitchMessageEvaluator(minidi.Injectable)