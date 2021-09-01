# vendor
import minidi

# local
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.module.ModuleList import ModuleList

class ModuleCallbackRunner(minidi.Injectable):
	pModuleFactory: ModuleFactory
	pModuleList: ModuleList

	def onBotStartup(self) -> bool:
		moduleClasses = self.pModuleList.getModuleClasses()

		for moduleClass in moduleClasses:
			pModuleClassInstance = self.pModuleFactory.createModule(moduleClass)
			success = pModuleClassInstance.onBotStartup()
			if not success:
				return False
		# for moduleClass in moduleClasses

		return True
	# def onBotStartup(self)

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