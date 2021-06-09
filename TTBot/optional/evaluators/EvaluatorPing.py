# local
from .Evaluator import Evaluator

class EvaluatorPing(Evaluator):
    @staticmethod
    def getMessageRegex() -> str:
        return r'\b(ping)\b'
    
    @staticmethod
    def getRightsId() -> str:
        return 'ping'
    
    async def execute(self) -> str:
        return 'pong'
# class EvaluatorPing(Evaluator)