# pylib
import os

# vendor
import minidi
from twitchio.ext import commands

# local
from TTBot.data.Message import Message
from TTBot.logic.Environment import Environment
from TTBot.logic.Logger import Logger
from TTBot.logic.interface.MessageConverter import MessageConverter
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.module.ModuleRunner import ModuleRunner

class TrackmaniaTwitchBot(commands.Bot):
    def __init__(self, **kwargs):
        self.pEnvironment          = kwargs.get('Environment'         , minidi.get(Environment))
        self.pLogger               = kwargs.get('Logger'              , minidi.get(Logger))
        self.pMessageConverter     = kwargs.get('MessageConverter'    , minidi.get(MessageConverter))
        self.pMessageEvaluator     = kwargs.get('MessageEvaluator'    , minidi.get(MessageEvaluator))
        self.pModuleCallbackRunner = kwargs.get('ModuleCallbackRunner', minidi.get(ModuleCallbackRunner))
        self.pModuleManager        = kwargs.get('ModuleManager'       , minidi.get(ModuleManager))
        self.pModuleRunner         = kwargs.get('ModuleRunner'        , minidi.get(ModuleRunner))

        super().__init__(
            token=self.pEnvironment.getVariable('TWITCH_ACCESS_TOKEN'),
            client_id=self.pEnvironment.getVariable('TWITCH_CLIENT_ID'),
            prefix=self.pEnvironment.getVariable('TWITCH_CMD_PREFIX')#,
            #initial_channels=['trackmania_bot'] # initial join doesnt currently work in twitchio
        )
        
        moduleInitSuccess = self.pModuleCallbackRunner.onBotStartup()
        if not moduleInitSuccess:
            self.pLogger.error("Module initialization failed!")
            os._exit(1)
        
        self.pLogger.info("Twitchio Bot successfully started!")
    # def __init__(self)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        self.pLogger.info(f'Logged in as | {self.nick}')

        channelList = self.getChannelList()
        if not channelList:
            raise RuntimeError("Could not boot TTBot, channel list is empty!")
            
        self.pLogger.info(f"Joining channels: \t{', '.join(channelList)} ...")

        try:
            await self.join_channels(channelList)
        except:
            self.pLogger.error("Could not join twitch channels!")
            self.pLogger.error(f"channelList: {channelList}")
            os._exit(1)
    # async def event_ready(self)

    def getChannelList(self) -> list:
        try:
            return self.pModuleManager.getChannels()
        except:
            self.pLogger.error("Could not extract channel list from DB!")
            self.pLogger.warning(f"Trying to insert own channel into DB...")
            twitchBotUsername = self.pEnvironment.getTwitchBotUsername()
            self.pModuleManager.addChannel(twitchBotUsername)
            os._exit(1)
    # def getChannelList(self) -> list
    
    async def event_message(self, pMessage):
        try:
            pMessage = self.pMessageConverter.convert(pMessage)
        except:
            return
        
        # Runs every time a message is sent to the channel
        # ignore non existent author (twitchio bug):
        if pMessage.getAuthor() is None:
            return
        
        # ignore thyself
        if self.pEnvironment.getTwitchBotUsername() == pMessage.getAuthor().getName().lower():
            self.pLogger.debug("Own message detected and ignored")
            return

        # handle commands and evaluations
        await self.handleMessage(pMessage)
    # async def event_message(self, pMessage)

    async def handleMessage(self, pMessage: Message):
        messageAuthorName = pMessage.getAuthor().getName()
        message = pMessage.getContent()
        self.pLogger.debug(f"{messageAuthorName}\t:{message}")

        await self.pModuleRunner.execute(pMessage)
    # async def handle(self, pMessage: Message)
# class TrackmaniaTwitchBot(commands.Bot)