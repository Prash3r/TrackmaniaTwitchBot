# pylib
from abc import abstractmethod

# local
from TTBot.data.Message import Message
from TTBot.module.Module import Module

class Command(Module):
	@abstractmethod
	def getCommandTrigger(self):
		pass

	@abstractmethod
	async def execute(self, pMessage: Message, args: list) -> str:
		pass
# class Command(Module)