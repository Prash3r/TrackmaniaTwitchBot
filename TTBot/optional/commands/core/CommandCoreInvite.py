# local
from .CommandCore import CommandCore
from TTBot.data.Message import Message
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper

class CommandCoreInvite(CommandCore):
    pDbConnector: DbConnector
    pTwitchBotWrapper: TwitchBotWrapper

    def getCommandString(self) -> str:
        return 'invite'
    
    async def execute(self, pMessage: Message, _) -> str:
        try:
            messageAuthorName = pMessage.getAuthor().getName()
            pTwitchBot = self.pTwitchBotWrapper.get()
            await pTwitchBot.join_channels([f'{messageAuthorName}'])

            self.pDbConnector.execute(f"INSERT IGNORE INTO modules (channel) VALUES ('{messageAuthorName}');")
            return f"@{messageAuthorName} I joined your channel, now you can control me over there!"
        except:
            return "kem1W"
    # async def execute(self, pMessage: Message, _) -> str
# class CommandCoreInvite(CommandCore)