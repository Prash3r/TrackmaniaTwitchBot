# pylib
import logging
import os

# vendor
import minidi
from twitchio.ext import commands

# local
from .logic.Environment import Environment
from .logic.Logger import Logger

class TrackmaniaTwitchBot(commands.Bot):
    from ._db import conn, creationcmds, tablelist, PV, DB, DB_connect, DB_init, DB_init_table, DB_init_processvars, DB_query, DB_GetPV, DB_WritePV
    from ._tools import sanitize, ownerrights, botchathome, isint, getUserLevel, rights
    from ._handle import handle

    def __init__(self):
        self.initLogger()
        pEnvironment: Environment = minidi.get(Environment)
        pLogger: Logger = minidi.get(Logger)

        super().__init__(
            token=pEnvironment.getVariable('TWITCH_ACCESS_TOKEN'),
            client_id=pEnvironment.getVariable('TWITCH_CLIENT_ID'),
            prefix=pEnvironment.getVariable('TWITCH_CMD_PREFIX')#,
            #intial_channels=['trackmania_bot'] # initial join doesnt currently work in twitchio
        )
        
        # get Database connection going
        self.DB_connect()
        self.DB_init()
        pLogger.info("Database initiated")
        # DB.query() callable from now on

        pLogger.info("Twitchio Bot initiated")
        return
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

        # We are logged in and ready to chat and use commands...
        pLogger.info(f'Logged in as | {self.nick}')
        channellist = []
        logentry = "joining the following channels on startup: \t"
        try:
            # join all channels present in the modules table:
            cur = self.DB_query("SELECT channel from modules")
            for channel in cur:
                channellist.append(channel[0])
                logentry += channel[0] + ', '
            
            logentry = logentry[:-2] # hackertricks
            pLogger.info(logentry)
            if not channellist:
                raise Exception("channellist was empty")
            
            await self.join_channels(channellist)
        except:
            pEnvironment: Environment = minidi.get(Environment)
            twitchBotUsername = pEnvironment.getTwitchBotUsername()

            pLogger.error("could not extract channel list from DB on startup")
            pLogger.error(f"channellist:{channellist}")
            #try to create create the bots channel in module table
            pLogger.warning(f"trying to get my on channel into DB")
            self.DB_query(f"INSERT IGNORE INTO modules(channel) VALUES('{twitchBotUsername}')")
            os._exit(1)
    # async def event_ready(self)
    
    async def event_message(self, ctx):
        # Runs every time a message is sent to the channel
        # ignore non existent author (twitchio bug):
        if ctx.author is None:
            return
        
        # ignore thyself
        pEnvironment: Environment = minidi.get(Environment)
        if ctx.author.name.lower() == pEnvironment.getTwitchBotUsername():
            logging.debug("own message detected and ignored")
            return

        # handle commands and evaluations
        await self.handle(ctx)
    # async def event_message(self, ctx)
# class TrackmaniaTwitchBot(commands.Bot)