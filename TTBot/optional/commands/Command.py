# pylib
from abc import abstractmethod

# local
from ..Module import Module

class Command(Module):
	@abstractmethod
	def getCommandString(self) -> str:
		pass

	@abstractmethod
	def execute(self, pMessage, args: list) -> str:
		pass
# class Command(Module)