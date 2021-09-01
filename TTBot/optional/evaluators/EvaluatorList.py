# vendor
import minidi

# local
from TTBot.module.luckers.EvaluatorLuckers import EvaluatorLuckers
from .EvaluatorOoga import EvaluatorOoga
from .EvaluatorPing import EvaluatorPing

class EvaluatorList(minidi.Injectable):
	def getAllEvaluatorClasses(self) -> list:
		return [
			# general evaluators
			EvaluatorPing,

			# personalized evaluators
			EvaluatorLuckers,
			EvaluatorOoga
		]
	# def getAllEvaluatorClasses(self) -> list
# class EvaluatorList(minidi.Injectable)