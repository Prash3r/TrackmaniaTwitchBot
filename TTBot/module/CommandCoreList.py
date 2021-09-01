# vendor
import minidi

# local
from TTBot.module.core.CommandCoreHelp import CommandCoreHelp
from TTBot.module.core.CommandCoreInvite import CommandCoreInvite
from TTBot.module.core.CommandCoreModule import CommandCoreModule
from TTBot.module.core.CommandCoreUninvite import CommandCoreUninvite
from TTBot.module.core.CommandCoreUpdate import CommandCoreUpdate

class CommandCoreList(minidi.Injectable):
	def getCommandCoreClasses(self) -> list:
		return [
			CommandCoreHelp,
			CommandCoreInvite,
			CommandCoreModule,
			CommandCoreUninvite,
			CommandCoreUpdate
		]
	# def getCommandCoreClasses(self) -> list
# class CommandCoreList(minidi.Injectable)