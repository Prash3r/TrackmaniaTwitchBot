# vendor
import minidi

# local
from .CommandJoke import CommandJoke
from TTBot.module.kem.CommandKem import CommandKem
from TTBot.module.matchmaking.CommandMm import CommandMm
from .CommandRoll import CommandRoll
from .CommandScore import CommandScore

class CommandList(minidi.Injectable):
	def getAllCommandClasses(self) -> list:
		return [
			CommandJoke,
			CommandKem,
			CommandMm,
			CommandRoll,
			CommandScore
		]
	# def getAllCommandClasses(self) -> list
# class CommandList(minidi.Injectable)