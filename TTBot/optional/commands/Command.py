# pylib
from abc import abstractmethod

# local
from TTBot.data.Message import Message
from ..Module import Module

class Command(Module):
	@abstractmethod
	def getCommandString(self) -> str:
		pass

	@abstractmethod
	def execute(self, pMessage: Message, args: list) -> str:
		pass
# class Command(Module)