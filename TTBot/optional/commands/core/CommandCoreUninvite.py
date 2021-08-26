# local
from .CommandCore import CommandCore
from TTBot.logic.MariaDbWrapper import MariaDbWrapper
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandCoreUninvite(CommandCore):
    pMariaDbWrapper: MariaDbWrapper
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'uninvite'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
            self.pMariaDbWrapper.query(f"DELETE FROM modules WHERE channel = '{messageAuthorName}';")
            return f"@{messageAuthorName} I left your channel, you can reinvite me in my channel!"
        except:
            return "kem1W"
    # async def execute(self, pMessage, _) -> str
# class CommandCoreUninvite(CommandCore)