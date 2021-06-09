# pylib
import random
# local
from .Command import Command

class CommandRoll(Command):
    
    @staticmethod
    def getCommandString() -> str:
        return 'roll'
    
    @staticmethod
    def getRightsId() -> str:
        return 'roll'

    async def execute(self, args) -> str:
        try:
            number = int(args[0])
            result = random.randint(1,number)
            if result == 69 :
                return f'{result}/{number} - NICE'
            elif number == 420 :
                return f'No, @{self.messageAuthor} - we do not support drugs in this chat ({result}/{number})'
            else:
                return f'{result}/{number}'
        except:
            pass

    