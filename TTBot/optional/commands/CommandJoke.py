# pylib
import random

# local
from .Command import Command
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandJoke(Command):
    FUNC_JOKE_USER_SPECIALS = {
        'fegir': lambda lastjoker: lastjoker,
        'amaterasutm': lambda _: 'kem1W' if random.random() >= 0.9 else 'you know who!'
    }
    FUNC_JOKE_DEFAULT = lambda messageAuthor: f"modCheck .. {messageAuthor} .. KEKW" if random.random() >= 0.9 else 'Fegir'

    pProcessVariables: ProcessVariables
    pTwitchMessageEvaluator: TwitchMessageEvaluator
    
    def getCommandString(self) -> str:
        return 'joke'
    
    def getRightsId(self) -> str:
        return 'joke'

    async def execute(self, pMessage, _) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        messageAuthorName = messageAuthorName.lower()

        lastjoker = self.pProcessVariables.get('lastjoker', 'fegir')
        self.pProcessVariables.write('lastjoker', messageAuthorName)

        if messageAuthorName in CommandJoke.FUNC_JOKE_USER_SPECIALS.keys():
            funcJokeUserSpecial = CommandJoke.FUNC_JOKE_USER_SPECIALS[messageAuthorName]
            return funcJokeUserSpecial(lastjoker)
        
        return CommandJoke.FUNC_JOKE_DEFAULT(messageAuthorName)
    # async def execute(self, pMessage, _) -> str
# class CommandJoke(Command)