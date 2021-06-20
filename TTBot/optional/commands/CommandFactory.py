# vendor
import minidi

# local
from .Command import Command
from .CommandCore import CommandCore
from .CommandJoke import CommandJoke
from .CommandMm import CommandMm
from TTBot.logic.MariaDbWrapper import MariaDbWrapper
from TTBot.logic.MatchmakingCache import MatchmakingCache
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.TrackmaniaIO import TrackmaniaIO
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandFactory:
	@staticmethod
	def create(commandClass, pTwitchBot, ctx) -> Command:
		pCommandInstance = commandClass()

		if isinstance(pCommandInstance, CommandMm):
			pCommandInstance.pMatchmakingCache = minidi.get(MatchmakingCache)
			pCommandInstance.pTrackmaniaIO = minidi.get(TrackmaniaIO)

		if isinstance(pCommandInstance, CommandJoke):
			pCommandInstance.pProcessVariables = minidi.get(ProcessVariables)
		
		if isinstance(pCommandInstance, CommandCore):
			pCommandInstance.pTwitchBot = pTwitchBot
			pCommandInstance.pMariaDbWrapper = minidi.get(MariaDbWrapper)
		
		pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
		pCommandInstance.message = pTwitchMessageEvaluator.getContent(ctx)
		pCommandInstance.messageAuthor = pTwitchMessageEvaluator.getAuthorName(ctx)
		pCommandInstance.messageChannel = pTwitchMessageEvaluator.getChannelName(ctx) # probably breaks for whispers

		return pCommandInstance
	# def create(CommandClass, pTwitchBot, ctx) -> Command
# class CommandFactory