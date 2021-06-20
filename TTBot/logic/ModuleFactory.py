# vendor
import minidi

# local
from TTBot.optional.commands.Command import Command
from TTBot.optional.evaluators.Evaluator import Evaluator

class ModuleFactory(minidi.Injectable):
	def createCommand(self, commandClass) -> Command:
		return minidi.get(commandClass)

	def createEvaluator(self, evaluatorClass) -> Evaluator:
		return minidi.get(evaluatorClass)
# class ModuleFactory(minidi.Injectable)