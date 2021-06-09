# local
from .Command import Command
from .CommandMm import CommandMm

class CommandFactory:
	@staticmethod
	def create(commandClass, pTwitchBot, ctx) -> Command:
		pCommandInstance = commandClass()

		if isinstance(pCommandInstance, CommandMm):
			pCommandInstance.funcDB_query = pTwitchBot.DB_query
		pCommandInstance.message = ctx.content
		pCommandInstance.messageAuthor = ctx.author.name
		pCommandInstance.messageChannel = ctx.channel.name # probably breaks for whispers

		return pCommandInstance
	# def create(CommandClass, pTwitchBot, ctx) -> Command
# class CommandFactory