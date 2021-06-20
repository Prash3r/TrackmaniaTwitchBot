# pylib
import random

# local
from .Command import Command
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandScore(Command):
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'score'
    
    def getRightsId(self) -> str:
        return 'score'

    async def execute(self, pMessage, _) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        result = random.randint(0, 100000)

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