# pylib
import logging
import os
import re

# vendor
from TTBot import _tools

# local
from .CommandFactory import CommandFactory
from .CommandJoke import CommandJoke
from .CommandKem import CommandKem
from .CommandMm import CommandMm
from .CommandRoll import CommandRoll
from .CommandScore import CommandScore


class CommandRunner:
	COMMANDS = [
		CommandJoke,
		CommandKem,
		CommandMm,
		CommandRoll,
		CommandScore,
	]

	async def execute(self, pTwitchBot, ctx) -> bool:
		# check if first char is the command char
		#if (ctx.content[:1] == os.environ['TWITCH_CMD_PREFIX']):
		if (ctx.content[:1] != pTwitchBot._prefix):
			return False # no command char -> no command, abort here
		# build the args
		args = ctx.content[1:].split()
		if len(args) < 1:
			return False # only a ! no text after that
		for commandClass in self.COMMANDS:
			if (commandClass.getCommandString() != args[0]):
				continue
			#args.pop(0) # get rid of the command itself and only carry arguments from now on
			if _tools.rights(pTwitchBot, ctx, commandClass.getRightsId()):
				pCommandInstance = CommandFactory.create(commandClass, pTwitchBot, ctx)
				try:
					if len(args) < 2:
						result = await pCommandInstance.execute([])
					else:
						result = await pCommandInstance.execute(args[1:])
					await ctx.channel.send(result)
					logging.info(f"{commandClass.__name__} did trigger")
				except Exception as e:
					logging.exception(e)
			# if _tools.rights(pTwitchBot, ctx, commandrClass.getRightsId())
		# for commandrClass in self.COMMANDS
	# def execute(self, ctx)
# class CommandRunner
