# pylib
import logging
import os

# vendor
import minidi
from twitchio.ext import commands

# local
from .logic.Environment import Environment
from .logic.Logger import Logger
from .logic.MariaDbConnection import MariaDbConnection
from .logic.MariaDbWrapper import MariaDbWrapper
from .logic.ModuleCallbackRunner import ModuleCallbackRunner
from .logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from .optional.commands.CommandRunner import CommandRunner
from .optional.evaluators.EvaluatorRunner import EvaluatorRunner

class TrackmaniaTwitchBot(commands.Bot):
    def __init__(self):
        self.initLogger()
        pLogger: Logger = minidi.get(Logger)

        pEnvironment: Environment = minidi.get(Environment)
        super().__init__(
            token=pEnvironment.getVariable('TWITCH_ACCESS_TOKEN'),
            client_id=pEnvironment.getVariable('TWITCH_CLIENT_ID'),
            prefix=pEnvironment.getVariable('TWITCH_CMD_PREFIX')#,
            #initial_channels=['trackmania_bot'] # initial join doesnt currently work in twitchio
        )
        
        pMariaDbConnection: MariaDbConnection = minidi.get(MariaDbConnection)
        pMariaDbConnection.connect()
        
        pModuleCallbackRunner: ModuleCallbackRunner = minidi.get(ModuleCallbackRunner)
        moduleInitSuccess = pModuleCallbackRunner.onBotStartup()
        if not moduleInitSuccess:
            pLogger.error("Module initialization failed!")
            os._exit(1)
        
        pLogger.info("Twitchio Bot successfully started!")
    # def __init__(self)
    
    def initLogger(self):
        pEnvironment: Environment = minidi.get(Environment)
        pLogger: Logger = minidi.get(Logger)

        pLogger.setLevel(logging.DEBUG if pEnvironment.isDebug() else logging.INFO)
        pFormatter = logging.Formatter("%(asctime)s [%(levelname)s.%(funcName)s] %(message)s")
        pStreamHandler = logging.StreamHandler()
        pStreamHandler.setFormatter(pFormatter)
        pLogger.addHandler(pStreamHandler)
    # def initLogger(self)

    async def event_ready(self):
        pLogger: Logger = minidi.get(Logger)
        pMariaDbWrapper: MariaDbWrapper = minidi.get(MariaDbWrapper)

        # We are logged in and ready to chat and use commands...
        pLogger.info(f'Logged in as | {self.nick}')
        channelList = []

        try:
            rows = pMariaDbWrapper.fetch("SELECT channel from modules")
            channelList = [row['channel'] for row in rows]
        except:
            pEnvironment: Environment = minidi.get(Environment)
            twitchBotUsername = pEnvironment.getTwitchBotUsername()

            pLogger.error("Could not extract channel list from DB!")
            pLogger.error(f"channelList: {channelList}")
            
            if twitchBotUsername not in channelList:
                pLogger.warning(f"Trying to insert own channel into DB...")
                pMariaDbWrapper.query(f"INSERT IGNORE INTO modules (channel) VALUES ('{twitchBotUsername}');")

            os._exit(1)
        # try fetch

        if not channelList:
            raise RuntimeError("Could not boot TTBot, channel list is empty!")
            
        pLogger.info(f"Joining channels: \t{', '.join(channelList)} ...")

        try:
            await self.join_channels(channelList)
        except:
            pLogger.error("Could not join twitch channels!")
            pLogger.error(f"channelList: {channelList}")
            os._exit(1)
    # async def event_ready(self)
    
    async def event_message(self, pMessage):
        # Runs every time a message is sent to the channel
        # ignore non existent author (twitchio bug):
        pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
        if pTwitchMessageEvaluator.getAuthor(pMessage) is None:
            return
        
        # ignore thyself
        if pTwitchMessageEvaluator.isBotAuthorOfMessage(pMessage):
            pLogger: Logger = minidi.get(Logger)
            pLogger.debug("own message detected and ignored")
            return

        # handle commands and evaluations
        await self.handleMessage(pMessage)
    # async def event_message(self, pMessage)

    async def handleMessage(self, pMessage):
        pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
        pLogger: Logger = minidi.get(Logger)
        pLogger.debug(f"{pTwitchMessageEvaluator.getAuthorName(pMessage)}\t:{pTwitchMessageEvaluator.getContent(pMessage)}")

        pCommandRunner: CommandRunner = minidi.get(CommandRunner)
        await pCommandRunner.execute(pMessage)

        pEvaluatorRunner: EvaluatorRunner = minidi.get(EvaluatorRunner)
        await pEvaluatorRunner.execute(pMessage)
    # async def handle(self, pMessage)
# class TrackmaniaTwitchBot(commands.Bot)