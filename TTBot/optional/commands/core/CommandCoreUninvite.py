# local
from .CommandCore import CommandCore
from TTBot.logic.MariaDbConnector import MariaDbConnector
from TTBot.logic.MessageEvaluator import MessageEvaluator

class CommandCoreUninvite(CommandCore):
    pMariaDbConnector: MariaDbConnector
    pMessageEvaluator: MessageEvaluator

    def getCommandString(self) -> str:
        return 'uninvite'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pMessageEvaluator.getAuthorName(pMessage)
            self.pMariaDbConnector.query(f"DELETE FROM modules WHERE channel = '{messageAuthorName}';")
            return f"@{messageAuthorName} I left your channel, you can reinvite me in my channel!"
        except:
            return "kem1W"
    # async def execute(self, pMessage, _) -> str
# class CommandCoreUninvite(CommandCore)