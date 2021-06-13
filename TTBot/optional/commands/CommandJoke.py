# pylib
import random
# local
from .Command import Command

class CommandJoke(Command):
    funcGetPV: callable
    funcWritePV: callable
    
    @staticmethod
    def getCommandString() -> str:
        return 'joke'
    
    @staticmethod
    def getRightsId() -> str:
        return 'joke'

    async def execute(self, args) -> str:
        lastjoker = self.funcGetPV('lastjoker')

        self.funcWritePV('lastjoker', self.messageAuthor, lastjoker)
        if self.messageAuthor.lower() == "fegir":
            return lastjoker
        if self.messageAuthor.lower() == "amaterasutm":
            if random.choice([True, False, False, False, False, False, False]):
                return 'kem1W'
            else:
                return 'you know who!'
        else:
            if random.choice([True, False, False, False, False, False, False]):
                return f"modCheck .. {self.messageAuthor} .. KEKW"
            else:
                return 'Fegir'