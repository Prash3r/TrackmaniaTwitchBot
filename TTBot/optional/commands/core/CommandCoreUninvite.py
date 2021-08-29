# local
from .CommandCore import CommandCore
from TTBot.data.Message import Message
from TTBot.logic.MariaDbConnector import MariaDbConnector

class CommandCoreUninvite(CommandCore):
    pMariaDbConnector: MariaDbConnector

    def getCommandString(self) -> str:
        return 'uninvite'
    
    async def execute(self, pMessage: Message, _) -> str:
        try:
            messageAuthorName = pMessage.getAuthor().getName()
            self.pMariaDbConnector.query(f"DELETE FROM modules WHERE channel = '{messageAuthorName}';")
            return f"@{messageAuthorName} I left your channel, you can reinvite me in my channel!"
        except:
            return "kem1W"
    # async def execute(self, pMessage: Message, _) -> str
# class CommandCoreUninvite(CommandCore)