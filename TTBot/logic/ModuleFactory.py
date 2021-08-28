# vendor
import minidi

# local
from TTBot.optional.commands.Command import Command
from TTBot.optional.evaluators.Evaluator import Evaluator
from TTBot.optional.Module import Module

class ModuleFactory(minidi.Injectable):
	def _create(self, cls):
		return minidi.get(cls)

	def createCommand(self, commandClass) -> Command:
		return self._create(commandClass)

	def createEvaluator(self, evaluatorClass) -> Evaluator:
		return self._create(evaluatorClass)

	def createModule(self, moduleClass) -> Module:
		return self._create(moduleClass)
# class ModuleFactory(minidi.Injectable)