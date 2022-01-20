# local
from TTBot.data.Message import Message
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.Randomizer import Randomizer
from TTBot.module.Command import Command

class CommandShitbot(Command):
    pGlobalVariables: GlobalVariables
    pRandomizer: Randomizer
    def getCommandTrigger(self):
        return 'shitbot'
    def getModuleId(self) -> str:
        return 'shitbot'

    def _getShitbotUserSpecials(self) -> dict:
        return {
            'scraken': self._shitbotUserSpecialScraken,
            'prash3r': self._shitbotUserSpecialMaster,
            'axelalex2': self._shitbotUserSpecialMaster,
        }
    # def _getshitbotUserSpecials(self) -> dict

    def _shitbotDefault(self) -> str:
        if self.pRandomizer.uniformFloat(0., 1.) >= 0.1:
            return "StreamElements ... WeirdChamping - a disgrace for all bots"
        else:
            return "Nightbot, how could you? That was such a moobot move ..."
    # def _shitbotDefault(self, messageAuthorName: str) -> str

    def _shitbotUserSpecialScraken(self) -> str:
        return "kem1W"
    # def _shitbotUserSpecialAmaterasu(self, _) -> str

    def _shitbotUserSpecialMaster(self) -> str:
        return "this hurts just a little ..."

    async def execute(self, pMessage: Message, _) -> str:
        messageAuthorName = pMessage.getAuthor().getName().lower()

        shitbotUserSpecials = self._getShitbotUserSpecials()

        if messageAuthorName in shitbotUserSpecials.keys():
            return shitbotUserSpecials[messageAuthorName]()
        # if messageAuthorName in shitbotUserSpecials.keys()
        return self._shitbotDefault()
    # async def execute(self, pMessage: Message, _) -> str
# class Commandshitbot(Command)
