# local
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel

class Message:
	def __init__(self, **kwargs):
		self._author = kwargs.get('author', None)
		self._channel = kwargs.get('channel', None)
		self._content = kwargs.get('content', '')
	# def __init__(self, **kwargs)

	def getAuthor(self) -> MessageAuthor:
		return self._author
	
	def getChannel(self) -> MessageChannel:
		return self._channel
	
	def getContent(self) -> str:
		return self._content
# class Message