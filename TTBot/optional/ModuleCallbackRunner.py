# vendor
import minidi

# local
from TTBot.logic.ModuleFactory import ModuleFactory
from .ModuleList import ModuleList

class ModuleCallbackRunner(minidi.Injectable):
	pModuleFactory: ModuleFactory
	pModuleList: ModuleList

	async def onBotStartup(self) -> bool:
		moduleClasses = self.pModuleList.getAllModuleClasses()

		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			success = await pModuleClassInstance.onBotStartup()
			if not success:
				return False
		# for moduleClass in moduleClasses

		return True
	# async def onBotStartup(self)

	def onModuleEnable(self, moduleName: str) -> bool:
		moduleClasses = self.pModuleList.getAllModuleClasses()

		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			if pModuleClassInstance.getRightsId() == moduleName:
				return pModuleClassInstance.onModuleEnable()
		# for moduleClass in moduleClasses

		return True
	# def onModuleEnable(self, moduleName: str)

	def onModuleDisable(self, moduleName: str) -> bool:
		moduleClasses = self.pModuleList.getAllModuleClasses()

		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			if pModuleClassInstance.getRightsId() == moduleName:
				return pModuleClassInstance.onModuleDisable()
		# for moduleClass in moduleClasses

		return True
	# def onModuleDisable(self, moduleName: str)
# class ModuleCallbackRunner