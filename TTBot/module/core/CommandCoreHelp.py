# local
from TTBot.data.Message import Message
from TTBot.module.core.CommandCore import CommandCore

class CommandCoreHelp(CommandCore):
    DEFAULT_HELP_MESSAGE = "Use '!help invite/uninvite/accesslevel/add/list/rem' for detailed information about this bots core commands!"
    HELP_MESSAGES = {
        'invite': "Use the command '!invite' to invite this bot to your channel!",
        'uninvite': "Use the command '!uninvite' to make the bot leave your channel!",
        'accesslevel': "Use the command '!module add modulename 10' to enable a module on your channel that can only be used by mods! (100=owner,10=moderators,5=subscribers,1=everyone)",
        'add': "Use the command '!module add modulename' to enable a module on your channel for everyone!",
        'list': "Use the command '!module list' to view the enabled modules on your channel!",
        'rem': "Use the command '!module rem' to disable the module on your channel!"
    }

    def getCommandTrigger(self):
        return 'help'
    
    async def execute(self, pMessage: Message, args: list) -> str:
        messageAuthorName = pMessage.getAuthor().getName()

        if args:
            return f"@{messageAuthorName} {self.HELP_MESSAGES.get(args[0], self.DEFAULT_HELP_MESSAGE)}"
                
        return f"@{messageAuthorName} {self.DEFAULT_HELP_MESSAGE}"
    # async def execute(self, pMessage: Message, args: list) -> str
# class CommandCoreHelp(CommandCore)