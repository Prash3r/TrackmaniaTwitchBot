# pylib
import random

# local
from .Command import Command
from TTBot.logic.ProcessVariables import ProcessVariables

class CommandJoke(Command):
    FUNC_JOKE_USER_SPECIALS = {
        'fegir': lambda lastjoker: lastjoker,
        'amaterasutm': lambda _: 'kem1W' if random.random() >= 0.9 else 'you know who!'
    }
    FUNC_JOKE_DEFAULT = lambda messageAuthor: f"modCheck .. {messageAuthor} .. KEKW" if random.random() >= 0.9 else 'Fegir'

    pProcessVariables: ProcessVariables
    
    @staticmethod
    def getCommandString() -> str:
        return 'joke'
    
    @staticmethod
    def getRightsId() -> str:
        return 'joke'

    async def execute(self, args: list) -> str:
        messageAuthor = self.messageAuthor.lower()

        lastjoker = self.pProcessVariables.get('lastjoker', 'fegir')
        self.pProcessVariables.write('lastjoker', messageAuthor)

        if messageAuthor in CommandJoke.FUNC_JOKE_USER_SPECIALS.keys():
            funcJokeUserSpecial = CommandJoke.FUNC_JOKE_USER_SPECIALS[messageAuthor]
            return funcJokeUserSpecial(lastjoker)
        
        return CommandJoke.FUNC_JOKE_DEFAULT(messageAuthor)
    # async def execute(self, args: list) -> str
# class CommandJoke(Command)