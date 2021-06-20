# pylib
import random

# local
from .Command import Command

class CommandScore(Command):
    @staticmethod
    def getCommandString() -> str:
        return 'score'
    
    @staticmethod
    def getRightsId() -> str:
        return 'score'

    async def execute(self, args: list) -> str:
        result = random.randint(0, 100000)

        if result == 69:
            return f"@{self.messageAuthor} has {result} LP - nice!"
        elif result == 42069:
            return f"@{self.messageAuthor} has {result} LP - NICE!"
        elif result == 69420:
            return f"@{self.messageAuthor} has {result} LP - MEGANICE!"
        elif '69' in str(result):
            return f"@{self.messageAuthor} has {result} LP - partly nice!"
        else:
            return f"@{self.messageAuthor} has {result} LP!"
    # async def execute(self, args: list) -> str
# class CommandScore(Command)