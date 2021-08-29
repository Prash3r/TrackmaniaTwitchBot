# local
from .Evaluator import Evaluator
from TTBot.data.Message import Message

class EvaluatorOoga(Evaluator):
    def getMessageRegex(self) -> str:
        return r'(ooga)\b'
    
    def getModuleId(self) -> str:
        return 'ooga'
    
    async def execute(self, _: Message) -> str:
        return 'booga'
# class EvaluatorOoga(Evaluator)