# local
from .CommandCore import CommandCore
from TTBot.logic.MariaDbConnector import MariaDbConnector
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper

class CommandCoreInvite(CommandCore):
    pMariaDbConnector: MariaDbConnector
    pMessageEvaluator: MessageEvaluator
    pTwitchBotWrapper: TwitchBotWrapper

    def getCommandString(self) -> str:
        return 'invite'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pMessageEvaluator.getAuthorName(pMessage)
            pTwitchBot = self.pTwitchBotWrapper.get()
            await pTwitchBot.join_channels([f'{messageAuthorName}'])

            self.pMariaDbConnector.query(f"INSERT IGNORE INTO modules (channel) VALUES ('{messageAuthorName}');")
            return f"@{messageAuthorName} I joined your channel, now you can control me over there!"
        except:
            return "kem1W"
    # async def execute(self, pMessage, _) -> str
# class CommandCoreInvite(CommandCore)