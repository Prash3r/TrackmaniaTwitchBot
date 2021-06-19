# vendor
import minidi
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.logic.UserRights import UserRights

# local
from .CommandCore import CommandInvite
from .CommandCore import CommandUninvite
from .CommandCore import CommandModule
from .CommandCore import CommandHelp
from .CommandFactory import CommandFactory
from .CommandJoke import CommandJoke
from .CommandKem import CommandKem
from .CommandMm import CommandMm
from .CommandRoll import CommandRoll
from .CommandScore import CommandScore


class CommandRunner:
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

	async def execute(self, pTwitchBot, ctx) -> bool:
		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
		content = pTwitchMessageEvaluator.getContent(ctx)
		if (content[:1] != pTwitchBot._prefix):
			return False # no command char -> no command, abort here
		
		pInputSanitizer: InputSanitizer = minidi.get(InputSanitizer)
		args = pInputSanitizer.sanitize(content[1:]).split()
		if len(args) < 1:
			return False # only a ! no text after that
		
		pLogger: Logger = minidi.get(Logger)
		pUserRights: UserRights = minidi.get(UserRights)

		for commandClass in self.COMMANDS:
			if (commandClass.getCommandString() != args[0]):
				continue
			#args.pop(0) # get rid of the command itself and only carry arguments from now on
			if pUserRights.allowModuleExecution(ctx, commandClass):
				pCommandInstance = CommandFactory.create(commandClass, pTwitchBot, ctx)
				try:
					if (args == None) or (len(args) < 2):
						result = await pCommandInstance.execute([])
					else:
						result = await pCommandInstance.execute(args[1:])

					await pTwitchMessageEvaluator.getChannel(ctx).send(result)
					pLogger.info(f"{commandClass.__name__} triggered by {pTwitchMessageEvaluator.getAuthorName(ctx)}")
				except Exception as e:
					pLogger.exception(e)
			# if pUserRights.allowModuleExecution(ctx, commandClass)
		# for commandClass in self.COMMANDS
	# def execute(self, ctx)
# class CommandRunner
