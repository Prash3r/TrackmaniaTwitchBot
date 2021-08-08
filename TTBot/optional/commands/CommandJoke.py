# local
from .Command import Command
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.Randomizer import Randomizer
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandJoke(Command):
    pProcessVariables: ProcessVariables
    pRandomizer: Randomizer
    pTwitchMessageEvaluator: TwitchMessageEvaluator
    
    def getCommandString(self) -> str:
        return 'joke'
    
    def getRightsId(self) -> str:
        return 'joke'
    
    def _getJokeUserSpecials(self) -> dict:
        return {
            'amaterasutm': self._jokeUserSpecialAmaterasu,
            'fegir': self._jokeUserSpecialFegir
        }
    # def _getJokeUserSpecials(self) -> dict
    
    def _jokeDefault(self, messageAuthorName: str) -> str:
        if self.pRandomizer.uniformFloat(0., 1.) >= 0.9:
            return f"modCheck .. {messageAuthorName} .. KEKW"
        
        return "Fegir"
    # def _jokeDefault(self, messageAuthorName: str) -> str

    def _jokeUserSpecialAmaterasu(self, _) -> str:
        if self.pRandomizer.uniformFloat(0., 1.) >= 0.9:
            return "kem1W"
        
        return "you know who!"
    # def _jokeUserSpecialAmaterasu(self, _) -> str

    def _jokeUserSpecialFegir(self, lastJoker: str) -> str:
        return lastJoker

    async def execute(self, pMessage, _) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        messageAuthorName = messageAuthorName.lower()

        jokeUserSpecials = self._getJokeUserSpecials()

        if messageAuthorName in jokeUserSpecials.keys():
            lastJoker = self.pProcessVariables.get('lastjoker', 'fegir')
            self.pProcessVariables.write('lastjoker', messageAuthorName)

            return jokeUserSpecials[messageAuthorName](lastJoker)
        # if messageAuthorName in jokeUserSpecials.keys()
        
        return self._jokeDefault(messageAuthorName)
    # async def execute(self, pMessage, _) -> str
# class CommandJoke(Command)