# local
from TTBot.data.Message import Message
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.module.core.CommandCore import CommandCore

class CommandCoreUninvite(CommandCore):
    pModuleManager: ModuleManager

    def getCommandTrigger(self):
        return 'uninvite'
    
    async def execute(self, pMessage: Message, _) -> str:
        try:
            messageAuthorName = pMessage.getAuthor().getName()
            self.pModuleManager.removeChannel(messageAuthorName)
            return f"@{messageAuthorName} I left your channel, you can reinvite me in my channel!"
        except:
            return "kem1W"
    # async def execute(self, pMessage: Message, _) -> str
# class CommandCoreUninvite(CommandCore)