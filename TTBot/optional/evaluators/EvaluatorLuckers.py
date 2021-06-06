# local
from .Evaluator import Evaluator

class EvaluatorLuckers(Evaluator):
    funcGetPV: callable
    funcWritePV: callable
    messageAuthor: str

    @staticmethod
    def getMessageRegex() -> str:
        return r'(luckers)\b'
    
    @staticmethod
    def getRightsId() -> str:
        return 'luckerscounter'
    
    async def execute(self) -> str:
        oldval = self.funcGetPV(self.getRightsId())
        newval = oldval + 1
        self.funcWritePV(self.getRightsId(), newval, oldval)
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{self.messageAuthor}!"
    # async def execute(self) -> str
# class EvaluatorLuckers(Evaluator)