# pylib
from abc import abstractmethod

# vendor
import minidi

# local
from TTBot.data.Message import Message

class MessageConverter(minidi.Injectable):
	@abstractmethod
	def convert(self, message) -> Message:
		pass
# class MessageConverter(minidi.Injectable)