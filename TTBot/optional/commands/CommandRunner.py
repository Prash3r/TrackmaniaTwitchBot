# vendor
import minidi

# local
from .Command import Command
from .core.CommandCoreList import CommandCoreList
from .CommandList import CommandList
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.logic.UserRights import UserRights

class CommandRunner(minidi.Injectable):
	pCommandCoreList: CommandCoreList
	pCommandList: CommandList
	pInputSanitizer: InputSanitizer
	pLogger: Logger
	pModuleFactory: ModuleFactory
	pTwitchBotWrapper: TwitchBotWrapper
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
			pChannel = pMessage.getChannel()
			await pChannel.sendMessage(result)
			messageAuthorName = pMessage.getAuthor().getName()
			self.pLogger.info(f"Command '{pCommand.getCommandString()}' triggered by {messageAuthorName}")
		except Exception as e:
			self.pLogger.exception(e)
	# async def _executeSingle(self, pCommand: Command, pMessage, args: list)

	async def _runPreChecks(self, pMessage):
		message = pMessage.getContent()
		pTwitchBot = self.pTwitchBotWrapper.get()

		if not message.startswith(pTwitchBot._prefix):
			return False
		
		message = message[len(pTwitchBot._prefix):]
		message = self.pInputSanitizer.sanitize(message)
		args = message.split()
		return args if args else False
	# async def _runPreChecks(self, pMessage)

	async def execute(self, pMessage) -> bool:
		args = await self._runPreChecks(pMessage)
		if not args:
			return False

		commandClasses = self.pCommandCoreList.getAllCommandCoreClasses() + self.pCommandList.getAllCommandClasses()

		for commandClass in commandClasses:
			pCommandClassInstance = self.pModuleFactory.createCommand(commandClass)
			await self._checkExecutionSingle(pCommandClassInstance, pMessage, args)
		# for commandClass in commandClasses

		return True
	# def execute(self, pMessage) -> bool
# class CommandRunner