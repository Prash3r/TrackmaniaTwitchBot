# local
from .Command import Command
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.Randomizer import Randomizer

class CommandScore(Command):
    pMessageEvaluator: MessageEvaluator
    pRandomizer: Randomizer

    def getCommandString(self) -> str:
        return 'score'
    
    def getModuleId(self) -> str:
        return 'score'

    async def execute(self, pMessage, _) -> str:
        messageAuthorName = self.pMessageEvaluator.getAuthorName(pMessage)
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
    # async def execute(self, pMessage, _) -> str
# class CommandScore(Command)