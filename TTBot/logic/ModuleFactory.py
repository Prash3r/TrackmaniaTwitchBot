# vendor
import minidi

# local
from TTBot.module.Command import Command
from TTBot.module.Evaluator import Evaluator
from TTBot.module.Module import Module

class ModuleFactory(minidi.Injectable):
	def createCommand(self, commandClass) -> Command:
		return minidi.get(commandClass)

	def createEvaluator(self, evaluatorClass) -> Evaluator:
		return minidi.get(evaluatorClass)

	def createModule(self, moduleClass) -> Module:
		return minidi.get(moduleClass)
# class ModuleFactory(minidi.Injectable)