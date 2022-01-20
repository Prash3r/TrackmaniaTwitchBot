# vendor
import minidi
import time

# local
from TTBot.logic.MessageSplitter import MessageSplitter

class MessageChannel:
	MAX_LENGTH = 500
	SPLITTERS = [' - ', '! ', '? ', '. ', ', ', '!', '?', '.', ',', '-', ' ']

	def __init__(self, **kwargs):
		self._name        = kwargs.get('name'       , '')
		self._sendMessage = kwargs.get('sendMessage', None)
	# def __init__(self, **kwargs)

	def getName(self) -> str:
		return self._name
	
	async def sendMessage(self, message: str):
		if not self._sendMessage:
			return
		
		pMessageSplitter: MessageSplitter = minidi.get(MessageSplitter)
		splits = pMessageSplitter.split(message, self.SPLITTERS, self.MAX_LENGTH)
		for split in splits:
			await self._sendMessage(split)
			time.sleep(0.2)
	# async def sendMessage(self, message: str)
# class MessageChannel