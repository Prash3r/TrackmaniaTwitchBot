# pylib
from abc import ABC, abstractmethod, abstractstaticmethod

class Evaluator(ABC):
	@staticmethod
	@abstractstaticmethod
	def getMessageRegex() -> str:
		pass

	@staticmethod
	@abstractstaticmethod
	def getRightsId() -> str:
		pass

	@abstractmethod
	async def execute(self) -> str:
		pass
# class Evaluator(ABC)