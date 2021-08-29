# local
from .CommandCore import CommandCore
from TTBot.logic.MessageEvaluator import MessageEvaluator

class CommandCoreHelp(CommandCore):
    DEFAULT_HELP_MESSAGE = "Use '!help invite/uninvite/accesslevel/add/list/rem' for detailed information about this bots core commands!"
    HELP_MESSAGES = {
        'invite': "Use the command '!invite' to invite this bot to your channel!",
        'uninvite': "Use the command '!uninvite' to make the bot leave your channel!",
        'accesslevel': "Use the command '!module add modulename 10' to enable a module on your channel with a minimum access level required!",
        'add': "Use the command '!module add modulename' to enable a module on your channel for everyone!",
        'list': "Use the command '!module list' to view the enabled modules on your channel!",
        'rem': "Use the command '!module rem' to disable the module on your channel!"
    }

    pMessageEvaluator: MessageEvaluator

    def getCommandString(self) -> str:
        return 'help'
    
    async def execute(self, pMessage, args: list) -> str:
        messageAuthorName = self.pMessageEvaluator.getAuthorName(pMessage)

        if args:
            return f"@{messageAuthorName} {self.HELP_MESSAGES.get(args[0], self.DEFAULT_HELP_MESSAGE)}"
                
        return f"@{messageAuthorName} {self.DEFAULT_HELP_MESSAGE}"
    # async def execute(self, pMessage, args: list) -> str
# class CommandCoreHelp(CommandCore)