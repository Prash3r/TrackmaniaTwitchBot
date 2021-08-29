# local
from .Evaluator import Evaluator
from TTBot.logic.GlobalVariables import GlobalVariables

class EvaluatorLuckers(Evaluator):
    pGlobalVariables: GlobalVariables

    def getMessageRegex(self) -> str:
        return r'(luckers)\b'
    
    def getModuleId(self) -> str:
        return 'luckerscounter'
    
    async def execute(self, pMessage) -> str:
        oldval = self.pGlobalVariables.get(self.getModuleId(), 0)
        newval = oldval + 1
        self.pGlobalVariables.write(self.getModuleId(), newval)

        messageAuthorName = pMessage.getAuthor().getName()
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{messageAuthorName}!"
    # async def execute(self, pMessage) -> str
# class EvaluatorLuckers(Evaluator)