# vendor
import minidi

# local
from .CommandJoke import CommandJoke
from .CommandKem import CommandKem
from .CommandMm import CommandMm
from .CommandRoll import CommandRoll
from .CommandScore import CommandScore

class CommandList(minidi.Injectable):
	def getAllCommandClasses(self) -> list:
		return [
			# general commands
			CommandMm,
			CommandRoll,
			CommandScore,

			# personalized commands
			CommandJoke,
			CommandKem
		]
	# def getAllCommandClasses(self) -> list
# class CommandList(minidi.Injectable)