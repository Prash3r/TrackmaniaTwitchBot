# pylib
import random

# vendor
import minidi

# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer

class CommandRoll(Command):
    @staticmethod
    def getCommandString() -> str:
        return 'roll'
    
    @staticmethod
    def getRightsId() -> str:
        return 'roll'

    async def execute(self, args) -> str:
        pInputSanitizer: InputSanitizer = minidi.get(InputSanitizer)
        if not args or not pInputSanitizer.isInteger(args[0]):
            return f"Use '!roll <max>' to roll a number out of max!"
        
        maxValue = int(args[0])
        result = random.randint(1, maxValue)

        if result == 69:
            return f"{result}/{maxValue} - NICE"
        elif maxValue == 420:
            return f"@{self.messageAuthor} we do not support drugs in this chat ({result}/{maxValue})"
        else:
            return f"{result}/{maxValue}"
    # async def execute(self, args) -> str
# class CommandRoll(Command)