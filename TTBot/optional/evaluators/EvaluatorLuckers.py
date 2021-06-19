# local
from .Evaluator import Evaluator
from TTBot.logic.MariaDbWrapper import MariaDbWrapper

class EvaluatorLuckers(Evaluator):
    pMariaDbWrapper: MariaDbWrapper
    messageAuthor: str

    @staticmethod
    def getMessageRegex() -> str:
        return r'(luckers)\b'
    
    @staticmethod
    def getRightsId() -> str:
        return 'luckerscounter'
    
    async def execute(self) -> str:
        oldval = self.pMariaDbWrapper.getProcessVariable(self.getRightsId())
        newval = oldval + 1
        self.pMariaDbWrapper.writeProcessVariable(self.getRightsId(), newval, oldval)
        return f"Turbo was called Luckers for {newval} times ... please just dont, @{self.messageAuthor}!"
    # async def execute(self) -> str
# class EvaluatorLuckers(Evaluator)