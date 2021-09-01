# local
from .Command import Command
from TTBot.data.Message import Message
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.Randomizer import Randomizer

class CommandJoke(Command):
    pGlobalVariables: GlobalVariables
    pRandomizer: Randomizer
    
    def getCommandString(self) -> str:
        return 'joke'
    
    def getModuleId(self) -> str:
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

    async def execute(self, pMessage: Message, _) -> str:
        messageAuthorName = pMessage.getAuthor().getName().lower()

        jokeUserSpecials = self._getJokeUserSpecials()

        if messageAuthorName in jokeUserSpecials.keys():
            lastJoker = self.pGlobalVariables.get('lastjoker', 'fegir')
            self.pGlobalVariables.write('lastjoker', messageAuthorName)

            return jokeUserSpecials[messageAuthorName](lastJoker)
        # if messageAuthorName in jokeUserSpecials.keys()
        
        return self._jokeDefault(messageAuthorName)
    # async def execute(self, pMessage: Message, _) -> str
# class CommandJoke(Command)