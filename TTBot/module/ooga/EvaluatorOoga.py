# local
from TTBot.data.Message import Message
from TTBot.module.Evaluator import Evaluator

class EvaluatorOoga(Evaluator):
    def getMessageRegex(self) -> str:
        return r'\b(ooga)\b'
    
    def getModuleId(self) -> str:
        return 'ooga'
    
    async def execute(self, _: Message) -> str:
        return 'booga'
# class EvaluatorOoga(Evaluator)