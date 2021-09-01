# pylib
import sys

# local
from TTBot.data.Message import Message
from TTBot.module.core.CommandCore import CommandCore

class CommandCoreUpdate(CommandCore):
    def getCommandTrigger(self):
        return 'update'
    
    async def execute(self, pMessage: Message, _) -> str:
        try:
            messageAuthorName = pMessage.getAuthor().getName()
            if messageAuthorName in ["axelalex2", "prash3r"]:
				# the system itself will reboot the bot for us
                sys.exit()
            else:
                return f"@{messageAuthorName}, you cannot make me do that!"
        except Exception:
            return "Going down failed miserably!"
    # async def execute(self, pMessage: Message, _) -> str
# class CommandCoreUpdate(CommandCore)