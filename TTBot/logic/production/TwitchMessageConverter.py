# vendor
import twitchio

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.interface.MessageConverter import MessageConverter

class TwitchMessageConverter(MessageConverter):
	def convert(self, pOriginalMessage: twitchio.Message) -> Message:
		pAuthor = MessageAuthor(
			isMod       =pOriginalMessage.author.is_mod,
			isSubscriber=pOriginalMessage.author.is_subscriber,
			name        =pOriginalMessage.author.name
		)

		pChannel = MessageChannel(
			name=pOriginalMessage.channel.name,
			sendMessage=pOriginalMessage.channel.send
		)

		pMessage = Message(
			author=pAuthor,
			channel=pChannel,
			content=pOriginalMessage.content
		)

		return pMessage
	# def convert(self, pOriginalMessage: twitchio.Message) -> Message
# class TwitchMessageConverter(MessageConverter)