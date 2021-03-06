# local
from TTBot.data.Message import Message
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.module.Command import Command

class CommandKem(Command):
    pInputSanitizer: InputSanitizer

    def getCommandTrigger(self):
        return 'kem'
    
    def getModuleId(self) -> str:
        return 'kem'

    async def execute(self, _: Message, args: list) -> str:
        count = int(args[0]) if args and self.pInputSanitizer.isInteger(args[0]) else 1
        count = min(max(1, count), 10) # force 1 <= count <= 10
        listCount = ['kem1W'] * count
        return ' '.join(listCount)
    # async def execute(self, _: Message, args: list) -> str
# class CommandKem(Command)