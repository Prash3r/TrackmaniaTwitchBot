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
    
    def getJokeUserSpecials(self) -> dict:
        return {
            'amaterasutm': self.jokeUserSpecialAmaterasu,
            'fegir': self.jokeUserSpecialFegir
        }
    # def getJokeUserSpecials(self) -> dict
    
    def jokeDefault(self, messageAuthorName: str) -> str:
        if self.pRandomizer.uniformFloat(0., 1.) >= 0.9:
            return f"modCheck .. {messageAuthorName} .. KEKW"
        
        return "Fegir"
    # def jokeDefault(self, messageAuthorName: str) -> str

    def jokeUserSpecialAmaterasu(self, _) -> str:
        if self.pRandomizer.uniformFloat(0., 1.) >= 0.9:
            return "kem1W"
        
        return "you know who!"
    # def jokeUserSpecialAmaterasu(self, _) -> str

    def jokeUserSpecialFegir(self, lastJoker: str) -> str:
        return lastJoker

    async def execute(self, pMessage, _) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        messageAuthorName = messageAuthorName.lower()

        jokeUserSpecials = self.getJokeUserSpecials()

        if messageAuthorName in jokeUserSpecials.keys():
            lastJoker = self.pProcessVariables.get('lastjoker', 'fegir')
            self.pProcessVariables.write('lastjoker', messageAuthorName)

            return jokeUserSpecials[messageAuthorName](lastJoker)
        # if messageAuthorName in jokeUserSpecials.keys()
        
        return self.jokeDefault(messageAuthorName)
    # async def execute(self, pMessage, _) -> str
# class CommandJoke(Command)