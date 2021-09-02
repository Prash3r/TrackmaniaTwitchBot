# pylib
from abc import abstractmethod

# local
from TTBot.data.Message import Message
from TTBot.module.Module import Module

class Evaluator(Module):
	@abstractmethod
	def getMessageRegex(self) -> str:
		pass

	@abstractmethod
	async def execute(self, pMessage: Message) -> str:
		pass
# class Evaluator(Module)