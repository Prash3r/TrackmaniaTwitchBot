# vendor
import minidi

# local
from TTBot.module.joke.CommandJoke import CommandJoke
from TTBot.module.karma.CommandKarma import CommandKarma
from TTBot.module.kem.CommandKem import CommandKem
from TTBot.module.matchmaking.CommandMm import CommandMm
from TTBot.module.roll.CommandRoll import CommandRoll
from TTBot.module.score.CommandScore import CommandScore

from TTBot.module.karma.EvaluatorKarma import EvaluatorKarma
from TTBot.module.luckers.EvaluatorLuckers import EvaluatorLuckers
from TTBot.module.ooga.EvaluatorOoga import EvaluatorOoga
from TTBot.module.ping.EvaluatorPing import EvaluatorPing

COMMAND_LIST = [
	CommandJoke,
	CommandKarma,
	CommandKem,
	CommandMm,
	CommandRoll,
	CommandScore
]

EVALUATOR_LIST = [
	EvaluatorKarma,
	EvaluatorLuckers,
	EvaluatorOoga,
	EvaluatorPing
]

MODULE_LIST = COMMAND_LIST + EVALUATOR_LIST
MODULE_ID_LIST = list(set([moduleClass().getModuleId() for moduleClass in MODULE_LIST]))

class ModuleList(minidi.Injectable):
	def getCommandClasses(self) -> list:
		return COMMAND_LIST
	
	def getEvaluatorClasses(self) -> list:
		return EVALUATOR_LIST

	def getModuleClasses(self) -> list:
		return MODULE_LIST
	
	def getModuleIds(self) -> list:
		return MODULE_ID_LIST
# class ModuleList(minidi.Injectable)