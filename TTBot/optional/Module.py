# pylib
from abc import abstractmethod

# vendor
import minidi

class Module(minidi.Injectable):
	@abstractmethod
	def getRightsId(self) -> str:
		pass

	async def onBotStartup(self) -> bool:
		pass

	def onModuleEnable(self) -> bool:
		pass

	def onModuleDisable(self) -> bool:
		pass
# class Module(minidi.Injectable)