# vendor
import minidi

# local
from .commands.CommandList import CommandList
from .evaluators.EvaluatorList import EvaluatorList

class ModuleList(minidi.Injectable):
	pCommandList: CommandList
	pEvaluatorList: EvaluatorList

	def getAllModuleClasses(self) -> list:
		return self.pCommandList.getAllCommandClasses() + self.pEvaluatorList.getAllEvaluatorClasses()
# class ModuleList(minidi.Injectable)