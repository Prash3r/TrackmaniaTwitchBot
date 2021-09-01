# pylib
import sys
import time

# local
from TTBot.data.Message import Message
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.module.core.CommandCore import CommandCore

class CommandCoreUpdate(CommandCore):
    pMessageEvaluator: MessageEvaluator
    pModuleManager: ModuleManager
    pTwitchBotWrapper: TwitchBotWrapper

    def getCommandTrigger(self):
        return 'update'
    
    async def execute(self, pMessage: Message, _) -> str:
        if not self.pMessageEvaluator.isDeveloperMessage(pMessage):
            return
        
        pChannel = pMessage.getChannel()
        pChannel.sendMessage("Rebooting ...")

        # ensure, that the message can be sent in time
        time.sleep(2)
        
        try:
            # the system itself will reboot the bot for us
            sys.exit()
        except Exception:
            return "Going down failed miserably!"
    # async def execute(self, pMessage: Message, _) -> str

    async def onBotStartup(self) -> bool:
        try:
            pTwitchBot = self.pTwitchBotWrapper.get()
            for pChannel in pTwitchBot.connected_channels:
                await pChannel.send("Successfully updated!")
        
            return True
        except:
            return False
    # async def onBotStartup(self) -> bool
# class CommandCoreUpdate(CommandCore)