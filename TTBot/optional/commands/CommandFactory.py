# local
from .Command import Command
from .CommandCore import CommandCore
from .CommandCore import CommandInvite
from .CommandMm import CommandMm

class CommandFactory:
	@staticmethod
	def create(commandClass, pTwitchBot, ctx) -> Command:
		pCommandInstance = commandClass()

		if isinstance(pCommandInstance, CommandMm):
			pCommandInstance.funcDB_query = pTwitchBot.DB_query
		
		if isinstance(pCommandInstance, CommandCore):
			pCommandInstance.pTwitchBot = pTwitchBot
			pCommandInstance.funcDB_query = pTwitchBot.DB_query
			pCommandInstance.pctx = ctx
		pCommandInstance.message = ctx.content
		pCommandInstance.messageAuthor = ctx.author.name
		pCommandInstance.messageChannel = ctx.channel.name # probably breaks for whispers

		return pCommandInstance
	# def create(CommandClass, pTwitchBot, ctx) -> Command
# class CommandFactory