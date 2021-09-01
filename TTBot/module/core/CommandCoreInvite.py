# local
from TTBot.data.Message import Message
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.module.core.CommandCore import CommandCore

class CommandCoreInvite(CommandCore):
    pModuleManager: ModuleManager
    pTwitchBotWrapper: TwitchBotWrapper

    def getCommandTrigger(self):
        return 'invite'
    
    async def execute(self, pMessage: Message, _) -> str:
        try:
            messageAuthorName = pMessage.getAuthor().getName()
            pTwitchBot = self.pTwitchBotWrapper.get()
            await pTwitchBot.join_channels([f'{messageAuthorName}'])

            self.pModuleManager.addChannel(messageAuthorName)
            return f"@{messageAuthorName} I joined your channel, now you can control me over there!"
        except:
            return "kem1W"
    # async def execute(self, pMessage: Message, _) -> str
# class CommandCoreInvite(CommandCore)