# local
from TTBot.data.Message import Message
from TTBot.module.Evaluator import Evaluator

class EvaluatorPing(Evaluator):
    def getMessageRegex(self) -> str:
        return r'\b(ping)\b'
    
    def getModuleId(self) -> str:
        return 'ping'
    
    async def execute(self, _: Message) -> str:
        return 'pong'
# class EvaluatorPing(Evaluator)