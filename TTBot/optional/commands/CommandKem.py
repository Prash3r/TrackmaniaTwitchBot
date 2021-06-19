# vendor
import minidi

# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer

class CommandKem(Command):
    @staticmethod
    def getCommandString() -> str:
        return 'kem'
    
    @staticmethod
    def getRightsId() -> str:
        return 'kem'

    async def execute(self, args: list) -> str:
        pInputSanitizer: InputSanitizer = minidi.get(InputSanitizer)

        count = args[0] if args and pInputSanitizer.isInteger(args[0]) else 1
        count = min(max(1, count), 10) # force 1 <= count <= 10
        listCount = ['kem1W'] * count
        return ' '.join(listCount)
    # async def execute(self, args: list) -> str
# class CommandKem(Command)