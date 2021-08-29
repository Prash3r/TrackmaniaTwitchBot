# local
from .Evaluator import Evaluator
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class EvaluatorLuckers(Evaluator):
    pGlobalVariables: GlobalVariables
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getMessageRegex(self) -> str:
        return r'(luckers)\b'
    
    def getModuleId(self) -> str:
        return 'luckerscounter'
    
    async def execute(self, pMessage) -> str:
        oldval = self.pGlobalVariables.get(self.getModuleId(), 0)
        newval = oldval + 1
        self.pGlobalVariables.write(self.getModuleId(), newval)

        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{messageAuthorName}!"
    # async def execute(self, pMessage) -> str
# class EvaluatorLuckers(Evaluator)