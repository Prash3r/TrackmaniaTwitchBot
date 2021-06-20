# vendor
import minidi

# local
from .Command import Command
from .CommandCore import CommandInvite
from .CommandCore import CommandUninvite
from .CommandCore import CommandModule
from .CommandCore import CommandHelp
from .CommandJoke import CommandJoke
from .CommandKem import CommandKem
from .CommandMm import CommandMm
from .CommandRoll import CommandRoll
from .CommandScore import CommandScore
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.logic.UserRights import UserRights

class CommandRunner(minidi.Injectable):
	COMMANDS = [
		CommandInvite,
		CommandUninvite,
		CommandModule,
		CommandHelp,
		CommandJoke,
		CommandKem,
		CommandMm,
		CommandRoll,
		CommandScore,
	]

	pInputSanitizer: InputSanitizer
	pLogger: Logger
	pTwitchMessageEvaluator: TwitchMessageEvaluator
	pUserRights: UserRights

	async def _checkExecutionSingle(self, pCommand: Command, pMessage, args: list):
		if pCommand.getCommandString() != args[0]:
			return

		if self.pUserRights.allowModuleExecution(pCommand, pMessage):
			await self._executeSingle(pCommand, pMessage, args[1:])
	# async def _checkExecutionSingle(self, pMessage, pCommand: Command)

	async def _executeSingle(self, pCommand: Command, pMessage, args: list):
		try:
			result = await pCommand.execute(pMessage, args)
			await self.pTwitchMessageEvaluator.getChannel(pMessage).send(result)
			messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
			self.pLogger.info(f"Command '{pCommand.getCommandString()}' triggered by {messageAuthorName}")
		except Exception as e:
			self.pLogger.exception(e)
	# async def _executeSingle(self, pCommand: Command, pMessage, args: list)

	async def execute(self, pTwitchBot, pMessage) -> bool:
		message = self.pTwitchMessageEvaluator.getContent(pMessage)

		if not message.startswith(pTwitchBot._prefix):
			return False
		
		message = message[len(pTwitchBot._prefix):]
		message = self.pInputSanitizer.sanitize(message)
		args = message.split()

		if not args:
			return False

		for commandClass in self.COMMANDS:
			await self._checkExecutionSingle(minidi.get(commandClass), pMessage, args)
	# def execute(self, ctx)
# class CommandRunner
