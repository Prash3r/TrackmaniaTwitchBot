# local
from .CommandCore import CommandCore
from TTBot.logic.MariaDbConnector import MariaDbConnector
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandCoreInvite(CommandCore):
    pMariaDbConnector: MariaDbConnector
    pTwitchBotWrapper: TwitchBotWrapper
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'invite'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
            pTwitchBot = self.pTwitchBotWrapper.get()
            await pTwitchBot.join_channels([f'{messageAuthorName}'])

            self.pMariaDbConnector.query(f"INSERT IGNORE INTO modules (channel) VALUES ('{messageAuthorName}');")
            return f"@{messageAuthorName} I joined your channel, now you can control me over there!"
        except:
            return "kem1W"
    # async def execute(self, pMessage, _) -> str
# class CommandCoreInvite(CommandCore)