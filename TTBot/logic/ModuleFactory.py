# vendor
import minidi

# local
from TTBot.optional.commands.Command import Command
from TTBot.optional.evaluators.Evaluator import Evaluator
from TTBot.optional.Module import Module

class ModuleFactory(minidi.Injectable):
	def createCommand(self, commandClass) -> Command:
		return minidi.get(commandClass)

	def createEvaluator(self, evaluatorClass) -> Evaluator:
		return minidi.get(evaluatorClass)

	def createModule(self, moduleClass) -> Module:
		return minidi.get(moduleClass)
# class ModuleFactory(minidi.Injectable)