# vendor
import minidi

# local
from TTBot.module.Command import Command
from TTBot.module.CommandCoreList import CommandCoreList
from TTBot.module.ModuleList import ModuleList
from TTBot.data.Message import Message
from TTBot.logic.Environment import Environment
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.logic.UserRights import UserRights

class CommandRunner(minidi.Injectable):
	pCommandCoreList: CommandCoreList
	pEnvironment: Environment
	pInputSanitizer: InputSanitizer
	pLogger: Logger
	pModuleFactory: ModuleFactory
	pModuleList: ModuleList
	pUserRights: UserRights

	async def _checkExecutionSingle(self, pCommand: Command, pMessage: Message, args: list):
		if pCommand.getCommandString() != args[0]:
			return

		if self.pUserRights.allowModuleExecution(pCommand, pMessage):
			await self._executeSingle(pCommand, pMessage, args[1:])
	# async def _checkExecutionSingle(self, pCommand: Command, pMessage: Message, args: list)

	async def _executeSingle(self, pCommand: Command, pMessage: Message, args: list):
		try:
			result = await pCommand.execute(pMessage, args)
			pChannel = pMessage.getChannel()
			await pChannel.sendMessage(result)
			messageAuthorName = pMessage.getAuthor().getName()
			self.pLogger.info(f"Command '{pCommand.getCommandString()}' triggered by {messageAuthorName}")
		except Exception as e:
			self.pLogger.exception(e)
	# async def _executeSingle(self, pCommand: Command, pMessage: Message, args: list)

	async def _runPreChecks(self, pMessage: Message):
		message = pMessage.getContent()
		commandPrefix = self.pEnvironment.getVariable('TWITCH_CMD_PREFIX')

		if not message.startswith(commandPrefix):
			return False
		
		message = message[len(commandPrefix):]
		message = self.pInputSanitizer.sanitize(message)
		args = message.split()
		return args if args else False
	# async def _runPreChecks(self, pMessage: Message)

	async def execute(self, pMessage: Message) -> bool:
		args = await self._runPreChecks(pMessage)
		if args is False:
			return False

		commandClasses = self.pCommandCoreList.getCommandCoreClasses() + self.pModuleList.getCommandClasses()

		for commandClass in commandClasses:
			pCommandClassInstance = self.pModuleFactory.createCommand(commandClass)
			await self._checkExecutionSingle(pCommandClassInstance, pMessage, args)
		# for commandClass in commandClasses

		return True
	# def execute(self, pMessage: Message) -> bool
# class CommandRunner