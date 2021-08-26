# vendor
import minidi

# local
from .CommandCoreHelp import CommandCoreHelp
from .CommandCoreInvite import CommandCoreInvite
from .CommandCoreModule import CommandCoreModule
from .CommandCoreUninvite import CommandCoreUninvite
from .CommandCoreUpdate import CommandCoreUpdate

class CommandCoreList(minidi.Injectable):
	def getAllCommandCoreClasses(self) -> list:
		return [
			CommandCoreHelp,
			CommandCoreInvite,
			CommandCoreModule,
			CommandCoreUninvite,
			CommandCoreUpdate
		]
	# def getAllCommandCoreClasses(self) -> list
# class CommandCoreList(minidi.Injectable)