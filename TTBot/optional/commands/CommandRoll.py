# pylib
import random

# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandRoll(Command):
    pInputSanitizer: InputSanitizer
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'roll'
    
    def getRightsId(self) -> str:
        return 'roll'

    async def execute(self, pMessage, args: list) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)

        if not args or not self.pInputSanitizer.isInteger(args[0]):
            return f"@{messageAuthorName} Use '!roll <max>' to roll a number out of max!"
        
        maxValue = int(args[0])
        result = random.randint(1, maxValue)

        if result == 69:
            return f"@{messageAuthorName} {result}/{maxValue} - NICE"
        elif maxValue == 420:
            return f"@{messageAuthorName} we do not support drugs in this chat ({result}/{maxValue})"
        else:
            return f"@{messageAuthorName} {result}/{maxValue}"
    # async def execute(self, pMessage, args: list) -> str
# class CommandRoll(Command)