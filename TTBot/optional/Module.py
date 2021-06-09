# pylib
from abc import ABC, abstractmethod, abstractstaticmethod

class Module(ABC):
	message: str
	messageAuthor: str
	messageChannel: str
	
	@staticmethod
	@abstractstaticmethod
	def getRightsId() -> str:
		pass

	@abstractmethod
	async def execute(self) -> str:
		pass
# class Command(ABC)