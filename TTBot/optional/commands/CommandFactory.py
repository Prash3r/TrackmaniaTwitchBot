# vendor
import minidi
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

# local
from .Command import Command
from .CommandCore import CommandCore
from .CommandJoke import CommandJoke
from .CommandMm import CommandMm

class CommandFactory:
	@staticmethod
	def create(commandClass, pTwitchBot, ctx) -> Command:
		pCommandInstance = commandClass()

		if isinstance(pCommandInstance, CommandMm):
			pCommandInstance.funcDB_query = pTwitchBot.DB_query

		if isinstance(pCommandInstance, CommandJoke):
			pCommandInstance.funcGetPV = pTwitchBot.DB_GetPV
			pCommandInstance.funcWritePV = pTwitchBot.DB_WritePV
		
		if isinstance(pCommandInstance, CommandCore):
			pCommandInstance.pTwitchBot = pTwitchBot
			pCommandInstance.funcDB_query = pTwitchBot.DB_query
			pCommandInstance.pctx = ctx
		
		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
		pCommandInstance.message = pTwitchMessageEvaluator.getContent(ctx)
		pCommandInstance.messageAuthor = pTwitchMessageEvaluator.getAuthorName(ctx)
		pCommandInstance.messageChannel = pTwitchMessageEvaluator.getChannelName(ctx) # probably breaks for whispers

		return pCommandInstance
	# def create(CommandClass, pTwitchBot, ctx) -> Command
# class CommandFactory