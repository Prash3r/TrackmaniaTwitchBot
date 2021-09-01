# local
from TTBot.data.Message import Message
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.module.Evaluator import Evaluator

class EvaluatorLuckers(Evaluator):
    pGlobalVariables: GlobalVariables

    def getMessageRegex(self) -> str:
        return r'(luckers)\b'
    
    def getModuleId(self) -> str:
        return 'luckerscounter'
    
    async def execute(self, pMessage: Message) -> str:
        oldval = self.pGlobalVariables.get(self.getModuleId(), 0)
        newval = oldval + 1
        self.pGlobalVariables.write(self.getModuleId(), newval)

        messageAuthorName = pMessage.getAuthor().getName()
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{messageAuthorName}!"
    # async def execute(self, pMessage: Message) -> str
# class EvaluatorLuckers(Evaluator)