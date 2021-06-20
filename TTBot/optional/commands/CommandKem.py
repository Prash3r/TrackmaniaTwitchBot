# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer

class CommandKem(Command):
    pInputSanitizer: InputSanitizer

    def getCommandString(self) -> str:
        return 'kem'
    
    def getRightsId(self) -> str:
        return 'kem'

    async def execute(self, _, args: list) -> str:
        count = args[0] if args and self.pInputSanitizer.isInteger(args[0]) else 1
        count = min(max(1, count), 10) # force 1 <= count <= 10
        listCount = ['kem1W'] * count
        return ' '.join(listCount)
    # async def execute(self, _, args: list) -> str
# class CommandKem(Command)