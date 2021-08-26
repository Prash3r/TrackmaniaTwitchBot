# pylib
import sys

# local
from .CommandCore import CommandCore
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class CommandCoreUpdate(CommandCore):
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'update'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
            if messageAuthorName in ["axelalex2", "prash3r"]:
				# the system itself will reboot the bot for us
                sys.exit()
            else:
                return f"@{messageAuthorName}, you cannot make me do that!"
        except Exception:
            return "Going down failed miserably!"
    # async def execute(self, pMessage, _) -> str
# class CommandCoreUpdate(CommandCore)