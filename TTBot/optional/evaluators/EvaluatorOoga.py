# local
from .Evaluator import Evaluator

class EvaluatorOoga(Evaluator):
    @staticmethod
    def getMessageRegex() -> str:
        return r'(ooga)\b'
    
    @staticmethod
    def getRightsId() -> str:
        return 'ooga'
    
    async def execute(self) -> str:
        return 'booga'
# class EvaluatorOoga(Evaluator)