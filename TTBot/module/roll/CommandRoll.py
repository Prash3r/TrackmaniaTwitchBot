# local
from TTBot.data.Message import Message
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Randomizer import Randomizer
from TTBot.module.Command import Command

class CommandRoll(Command):
    pInputSanitizer: InputSanitizer
    pRandomizer: Randomizer

    def getCommandTrigger(self):
        return 'roll'
    
    def getModuleId(self) -> str:
        return 'roll'

    async def execute(self, pMessage: Message, args: list) -> str:
        messageAuthorName = pMessage.getAuthor().getName()

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
    # async def execute(self, pMessage: Message, args: list) -> str
# class CommandRoll(Command)