# local
from .Evaluator import Evaluator

class EvaluatorOoga(Evaluator):
    def getMessageRegex(self) -> str:
        return r'(ooga)\b'
    
    def getModuleId(self) -> str:
        return 'ooga'
    
    async def execute(self, _) -> str:
        return 'booga'
# class EvaluatorOoga(Evaluator)