# pylib
from abc import abstractmethod

# local
from ..Module import Module

class Evaluator(Module):
	@abstractmethod
	def getMessageRegex(self) -> str:
		pass

	@abstractmethod
	def execute(self, pMessage) -> str:
		pass
# class Evaluator(Module)