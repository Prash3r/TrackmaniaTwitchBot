# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.interface.MessageConverter import MessageConverter

async def _asyncPrint(message: str):
	print(message)

class TerminalMessageConverter(MessageConverter):
	def convert(self, message) -> Message:
		pAuthor = MessageAuthor(isMod=True, isSubscriber=True, name='terminal')
		pChannel = MessageChannel(name='terminal', sendMessage=_asyncPrint)
		pMessage = Message(author=pAuthor, channel=pChannel, content=message)
		return pMessage
	# def convert(self, message) -> Message
# class TerminalMessageConverter(MessageConverter)