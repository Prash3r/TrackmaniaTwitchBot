# pylib
from abc import abstractmethod

# local
from ..Module import Module
from TTBot.data.Message import Message

class Evaluator(Module):
	@abstractmethod
	def getMessageRegex(self) -> str:
		pass

	@abstractmethod
	def execute(self, pMessage: Message) -> str:
		pass
# class Evaluator(Module)