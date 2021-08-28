# pylib
from abc import abstractmethod

# vendor
import minidi

class Module(minidi.Injectable):
	@abstractmethod
	def getModuleId(self) -> str:
		pass

	def onBotStartup(self) -> bool:
		return True

	def onModuleEnable(self):
		pass

	def onModuleDisable(self):
		pass
# class Module(minidi.Injectable)