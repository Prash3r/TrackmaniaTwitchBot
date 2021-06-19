# pylib
import random

# local
from .Command import Command
from TTBot.logic.ProcessVariables import ProcessVariables

class CommandJoke(Command):
    pProcessVariables: ProcessVariables
    
    @staticmethod
    def getCommandString() -> str:
        return 'joke'
    
    @staticmethod
    def getRightsId() -> str:
        return 'joke'

    async def execute(self, args) -> str:
        lastjoker = self.pProcessVariables.get('lastjoker', 'fegir')
        self.pProcessVariables.write('lastjoker', self.messageAuthor)

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