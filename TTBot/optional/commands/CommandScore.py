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

    async def execute(self, args) -> str:
        result = random.randint(0,100000)
        if result == 69:
            return f'{result} - NICE'
        if result == 69420:
            return f'{result} - MEGANICE'
        elif ('69' in str(result)):
            return f'{result} - partly nice'
        else:
            return f'{result}'