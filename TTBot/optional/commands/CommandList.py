# vendor
import minidi

# local
from .CommandCore import CommandHelp, CommandInvite, CommandModule, CommandUninvite, CommandUpdate
from .CommandJoke import CommandJoke
from .CommandKem import CommandKem
from .CommandMm import CommandMm
from .CommandRoll import CommandRoll
from .CommandScore import CommandScore

class CommandList(minidi.Injectable):
	def getAllCommandClasses(self) -> list:
		return [
			# core commands
			CommandUpdate,
			CommandHelp,
			CommandInvite,
			CommandModule,
			CommandUninvite,

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