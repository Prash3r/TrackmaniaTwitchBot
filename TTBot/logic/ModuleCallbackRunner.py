# vendor
import minidi

# local
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.module.ModuleList import ModuleList

class ModuleCallbackRunner(minidi.Injectable):
	pModuleFactory: ModuleFactory
	pModuleList: ModuleList

	async def onBotStartup(self, moduleClasses: list) -> bool:
		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			success = await pModuleClassInstance.onBotStartup()
			if not success:
				return False
		# for moduleClass in moduleClasses

		return True
	# async def onBotStartup(self, moduleClasses: list)

	def onModuleEnable(self, moduleName: str):
		moduleClasses = self.pModuleList.getModuleClasses()

		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			if pModuleClassInstance.getModuleId() == moduleName:
				pModuleClassInstance.onModuleEnable()
		# for moduleClass in moduleClasses
	# def onModuleEnable(self, moduleName: str)

	def onModuleDisable(self, moduleName: str):
		moduleClasses = self.pModuleList.getModuleClasses()

		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			if pModuleClassInstance.getModuleId() == moduleName:
				pModuleClassInstance.onModuleDisable()
		# for moduleClass in moduleClasses
	# def onModuleDisable(self, moduleName: str)
# class ModuleCallbackRunner