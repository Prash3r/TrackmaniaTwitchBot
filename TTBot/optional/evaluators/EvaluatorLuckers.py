# local
from .Evaluator import Evaluator
from TTBot.logic.ProcessVariables import ProcessVariables

class EvaluatorLuckers(Evaluator):
    pProcessVariables: ProcessVariables
    messageAuthor: str

    @staticmethod
    def getMessageRegex() -> str:
        return r'(luckers)\b'
    
    @staticmethod
    def getRightsId() -> str:
        return 'luckerscounter'
    
    async def execute(self) -> str:
        oldval = self.pProcessVariables.get(self.getRightsId(), 0)
        newval = oldval + 1
        self.pProcessVariables.write(self.getRightsId(), newval)
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{self.messageAuthor}!"
    # async def execute(self) -> str
# class EvaluatorLuckers(Evaluator)