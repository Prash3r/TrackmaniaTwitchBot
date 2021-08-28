# pylib
import os

# vendor
import minidi
from twitchio.ext import commands

# local
from .logic.Environment import Environment
from .logic.Logger import Logger
from .logic.MariaDbConnector import MariaDbConnector
from .logic.ModuleCallbackRunner import ModuleCallbackRunner
from .logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from .optional.commands.CommandRunner import CommandRunner
from .optional.evaluators.EvaluatorRunner import EvaluatorRunner

class TrackmaniaTwitchBot(commands.Bot):
    def __init__(self, **kwargs):
        self.pCommandRunner          = kwargs.get('CommandRunner'         , minidi.get(CommandRunner))
        self.pEnvironment            = kwargs.get('Environment'           , minidi.get(Environment))
        self.pEvaluatorRunner        = kwargs.get('EvaluatorRunner'       , minidi.get(EvaluatorRunner))
        self.pLogger                 = kwargs.get('Logger'                , minidi.get(Logger))
        self.pMariaDbConnector       = kwargs.get('MariaDbConnector'      , minidi.get(MariaDbConnector))
        self.pModuleCallbackRunner   = kwargs.get('ModuleCallbackRunner'  , minidi.get(ModuleCallbackRunner))
        self.pTwitchMessageEvaluator = kwargs.get('TwitchMessageEvaluator', minidi.get(TwitchMessageEvaluator))

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
            rows = self.pMariaDbConnector.fetch("SELECT `channel` FROM `modules`;")
            return [row['channel'] for row in rows]
        except:
            twitchBotUsername = self.pEnvironment.getTwitchBotUsername()
            self.pLogger.error("Could not extract channel list from DB!")
            self.pLogger.warning(f"Trying to insert own channel into DB...")
            self.pMariaDbConnector.query(f"INSERT IGNORE INTO `modules` (`channel`) VALUES ('{twitchBotUsername}');")
            os._exit(1)
    # def getChannelList(self) -> list
    
    async def event_message(self, pMessage):
        # Runs every time a message is sent to the channel
        # ignore non existent author (twitchio bug):
        if self.pTwitchMessageEvaluator.getAuthor(pMessage) is None:
            return
        
        # ignore thyself
        if self.pTwitchMessageEvaluator.isBotAuthorOfMessage(pMessage):
            self.pLogger.debug("own message detected and ignored")
            return

        # handle commands and evaluations
        await self.handleMessage(pMessage)
    # async def event_message(self, pMessage)

    async def handleMessage(self, pMessage):
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        message = self.pTwitchMessageEvaluator.getContent(pMessage)
        self.pLogger.debug(f"{messageAuthorName}\t:{message}")

        await self.pCommandRunner.execute(pMessage)
        await self.pEvaluatorRunner.execute(pMessage)
    # async def handle(self, pMessage)
# class TrackmaniaTwitchBot(commands.Bot)