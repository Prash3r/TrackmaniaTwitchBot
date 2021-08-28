# local
from .Evaluator import Evaluator
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class EvaluatorLuckers(Evaluator):
    pProcessVariables: ProcessVariables
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getMessageRegex(self) -> str:
        return r'(luckers)\b'
    
    def getModuleId(self) -> str:
        return 'luckerscounter'
    
    async def execute(self, pMessage) -> str:
        oldval = self.pProcessVariables.get(self.getModuleId(), 0)
        newval = oldval + 1
        self.pProcessVariables.write(self.getModuleId(), newval)

        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{messageAuthorName}!"
    # async def execute(self, pMessage) -> str
# class EvaluatorLuckers(Evaluator)