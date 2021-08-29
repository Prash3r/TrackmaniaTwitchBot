# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.Randomizer import Randomizer

class CommandRoll(Command):
    pInputSanitizer: InputSanitizer
    pMessageEvaluator: MessageEvaluator
    pRandomizer: Randomizer

    def getCommandString(self) -> str:
        return 'roll'
    
    def getModuleId(self) -> str:
        return 'roll'

    async def execute(self, pMessage, args: list) -> str:
        messageAuthorName = self.pMessageEvaluator.getAuthorName(pMessage)

        if not args or not self.pInputSanitizer.isInteger(args[0]):
            return f"@{messageAuthorName} Use '!roll <max>' to roll a number out of max!"
        
        maxValue = int(args[0])
        result = self.pRandomizer.uniformInt(1, maxValue)

        if result == 69:
            return f"@{messageAuthorName} {result}/{maxValue} - NICE"
        elif maxValue == 420:
            return f"@{messageAuthorName} we do not support drugs in this chat ({result}/{maxValue})"
        else:
            return f"@{messageAuthorName} {result}/{maxValue}"
    # async def execute(self, pMessage, args: list) -> str
# class CommandRoll(Command)