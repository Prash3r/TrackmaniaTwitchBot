# pylib
from abc import abstractmethod

# vendor
import minidi

class Module(minidi.Injectable):
	@abstractmethod
	def getRightsId(self) -> str:
		pass

	def onBotStartup(self) -> bool:
		return True

	def onModuleEnable(self) -> bool:
		return True

	def onModuleDisable(self) -> bool:
		return True
# class Module(minidi.Injectable)