# pylib
import os
import time
import traceback

# vendor
import minidi
from twitchio.ext import commands

# local
from TTBot.data.Message import Message
from TTBot.logic.interface.MessageConverter import MessageConverter
from TTBot.logic.Environment import Environment
from TTBot.logic.Logger import Logger
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.module.CommandCoreList import CommandCoreList
from TTBot.module.ModuleList import ModuleList
from TTBot.module.ModuleRunner import ModuleRunner

class TrackmaniaTwitchBot(commands.Bot):
    def __init__(self):
        pEnvironment: Environment = minidi.get(Environment)

        super().__init__(
            token=pEnvironment.getVariable('TWITCH_ACCESS_TOKEN'),
            client_id=pEnvironment.getVariable('TWITCH_CLIENT_ID'),
            prefix=pEnvironment.getVariable('TWITCH_CMD_PREFIX')#,
            #initial_channels=['trackmania_bot'] # initial join doesnt currently work in twitchio
        )
        
        pLogger: Logger = minidi.get(Logger)
        pLogger.info("Twitchio Bot successfully started!")
    # def __init__(self)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        pLogger: Logger = minidi.get(Logger)
        pLogger.info(f'Logged in as | {self.nick}')

        channelList = self.getChannelList()
        if not channelList:
            raise RuntimeError("Could not boot TTBot, channel list is empty!")
            
        pLogger.info(f"Joining channels: \t{', '.join(channelList)} ...")

        try:
            await self.join_channels(channelList)
        except:
            pLogger.error("Could not join twitch channels!")
            pLogger.error(f"channelList: {channelList}")
            os._exit(1)
        
        # ensure, that channels have been joined in time, so Modules can do anything they need to
        time.sleep(2)

        pCommandCoreList: CommandCoreList = minidi.get(CommandCoreList)
        pModuleList: ModuleList = minidi.get(ModuleList)
        moduleClasses = pCommandCoreList.getCommandCoreClasses() + pModuleList.getModuleClasses()

        pModuleCallbackRunner: ModuleCallbackRunner = minidi.get(ModuleCallbackRunner)
        moduleInitSuccess = await pModuleCallbackRunner.onBotStartup(moduleClasses)
        if not moduleInitSuccess:
            pLogger.error("Module initialization failed!")
            os._exit(1)
    # async def event_ready(self)

    def getChannelList(self) -> list:
        pLogger: Logger = minidi.get(Logger)
        pModuleManager: ModuleManager = minidi.get(ModuleManager)

        try:
            return pModuleManager.getChannels()
        except:
            pLogger.error("Could not extract channel list from DB!")
            pLogger.warning("Trying to insert own channel into DB...")

            pEnvironment: Environment = minidi.get(Environment)
            twitchBotUsername = pEnvironment.getTwitchBotUsername()
            pModuleManager.addChannel(twitchBotUsername)
            
            pLogger.info("Restart the bot to join its own channel!")

            os._exit(1)
    # def getChannelList(self) -> list
    
    async def event_message(self, pMessage):
        pMessageConverter: MessageConverter = minidi.get(MessageConverter)

        try:
            pMessage = pMessageConverter.convert(pMessage)
        except:
            return
        
        # Runs every time a message is sent to the channel
        # ignore non existent author (twitchio bug):
        if pMessage.getAuthor() is None:
            return
        
        pEnvironment: Environment = minidi.get(Environment)
        pLogger: Logger = minidi.get(Logger)
        # ignore thyself
        if pEnvironment.getTwitchBotUsername() == pMessage.getAuthor().getName().lower():
            pLogger.debug("self message, ignoring")
            return

        # handle commands and evaluations
        await self.handleMessage(pMessage)
    # async def event_message(self, pMessage)

    async def handleMessage(self, pMessage: Message):
        messageAuthorName = pMessage.getAuthor().getName()
        message = pMessage.getContent()

        pLogger: Logger = minidi.get(Logger)
        pLogger.debug(f"{messageAuthorName}\t:{message}")

        pModuleRunner: ModuleRunner = minidi.get(ModuleRunner)
        try:
            await pModuleRunner.execute(pMessage)
        except:
            pEnvironment: Environment = minidi.get(Environment)
            pMessageEvaluator: MessageEvaluator = minidi.get(MessageEvaluator)

            isBotChannel = pMessage.getChannel().getName() == pEnvironment.getTwitchBotUsername()
            if isBotChannel and pMessageEvaluator.isMainDeveloperMessage(pMessage):
                pMessage.getChannel().sendMessage(traceback.format_exc())
            
            raise
    # async def handle(self, pMessage: Message)
# class TrackmaniaTwitchBot(commands.Bot)