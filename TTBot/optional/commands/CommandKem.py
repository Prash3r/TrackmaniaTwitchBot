# local
from .Command import Command

class CommandKem(Command):
    
    @staticmethod
    def getCommandString() -> str:
        return 'kem'
    
    @staticmethod
    def getRightsId() -> str:
        return 'kem'

    async def execute(self, args) -> str:
        reply = 'kem1W'
        try:
            number = int(args[0])
            if number > 10:
                number = 10
            while (number > 1):
                number = number - 1
                reply = reply + ' kem1W'
        except:
            reply = 'kem1W'
        return reply