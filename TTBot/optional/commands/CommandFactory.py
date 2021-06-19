# vendor
import minidi

# local
from .Command import Command
from .CommandCore import CommandCore
from .CommandJoke import CommandJoke
from .CommandMm import CommandMm
from TTBot.logic.MariaDbWrapper import MariaDbWrapper
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandFactory:
	@staticmethod
	def create(commandClass, pTwitchBot, ctx) -> Command:
		pCommandInstance = commandClass()
		pMariaDbWrapper: MariaDbWrapper = minidi.get(MariaDbWrapper)

		if isinstance(pCommandInstance, CommandMm):
			pCommandInstance.pMariaDbWrapper = pMariaDbWrapper

		if isinstance(pCommandInstance, CommandJoke):
			pCommandInstance.pProcessVariables = minidi.get(ProcessVariables)
		
		if isinstance(pCommandInstance, CommandCore):
			pCommandInstance.pTwitchBot = pTwitchBot
			pCommandInstance.pMariaDbWrapper = pMariaDbWrapper
			pCommandInstance.pctx = ctx
		
		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
		pCommandInstance.message = pTwitchMessageEvaluator.getContent(ctx)
		pCommandInstance.messageAuthor = pTwitchMessageEvaluator.getAuthorName(ctx)
		pCommandInstance.messageChannel = pTwitchMessageEvaluator.getChannelName(ctx) # probably breaks for whispers

		return pCommandInstance
	# def create(CommandClass, pTwitchBot, ctx) -> Command
# class CommandFactory