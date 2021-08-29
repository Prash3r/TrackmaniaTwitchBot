# local
from .Command import Command
from TTBot.data.Message import Message
from TTBot.logic.Randomizer import Randomizer

class CommandScore(Command):
    pRandomizer: Randomizer

    def getCommandString(self) -> str:
        return 'score'
    
    def getModuleId(self) -> str:
        return 'score'

    async def execute(self, pMessage: Message, _) -> str:
        messageAuthorName = pMessage.getAuthor().getName()
        result = self.pRandomizer.uniformInt(0, 100000)

        if result == 69:
            return f"@{messageAuthorName} has {result} LP - nice!"
        elif result == 42069:
            return f"@{messageAuthorName} has {result} LP - NICE!"
        elif result == 69420:
            return f"@{messageAuthorName} has {result} LP - MEGANICE!"
        elif '69' in str(result):
            return f"@{messageAuthorName} has {result} LP - partly nice!"
        else:
            return f"@{messageAuthorName} has {result} LP!"
    # async def execute(self, pMessage: Message, _) -> str
# class CommandScore(Command)