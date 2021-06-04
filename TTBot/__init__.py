from twitchio.ext import commands
import os
import logging

class TrackmaniaTwitchBot(commands.Bot):
    from ._db import conn, creationcmds, tablelist, PV, DB, DB_connect, DB_init, DB_init_table, DB_init_processvars, DB_query, DB_GetPV, DB_WritePV
    from ._tools import sanitize, ownerrights, botchathome, isint, getUserLevel, rights
    from ._handle import handle
    from ._corecmds import CMD_help, CMD_invite, CMD_module, CMD_uninvite, CMD_test
    # commands imported into the Bot class right here:
    # (correctly decorated these should trigger automatically with no further action)
    from .optional.commands.joke import CMD_joke
    from .optional.commands.kem import CMD_kem
    from .optional.commands.mm import CMD_mm
    from .optional.commands.roll import CMD_roll
    from .optional.commands.score import CMD_score
    # general evaluators imported into the Bot class right here:
    # these need to be manually called from the _handle.py file
    # dont forget the rights check which also is the opt out for channels
    from .optional.evaluators.luckerscounter import EVAL_luckerscounter
    from .optional.evaluators.ooga import EVAL_ooga
    from .optional.evaluators.ping import EVAL_ping

    def __init__(self):
        # logging configuration
        if os.environ['DEBUG'] == "True":
            logginglevel = logging.DEBUG # Spam info
        else:
            logginglevel = logging.INFO # riolu info (only the result, u get it?)
            # maybe add rotating logsfile config here
        logging.basicConfig(
            level=logginglevel,
            format="%(asctime)s [%(levelname)s.%(funcName)s] %(message)s",
            handlers=[
                #logging.FileHandler("debug.log"),
                logging.StreamHandler()
            ]
        )
        super().__init__(
            token=os.environ['TWITCH_ACCESS_TOKEN'],
            client_id=os.environ['TWITCH_CLIENT_ID'],
            prefix=os.environ['TWITCH_CMD_PREFIX']#,
            #intial_channels=['trackmania_bot'] # initial join doesnt currently work in twitchio
        )
        
        # get Database connection going
        self.DB_connect()
        self.DB_init()
        logging.info("Database initiated")
        # DB.query() callable from now on

        logging.info("Twitchio Bot initiated")
        return

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        channellist = []
        logentry = "joining the following channels on startup: \t"
        try:
            # join all channels present in the modules table:
            cur = self.DB_query("SELECT channel from modules")
            for (channel) in cur:
                channellist.append(channel[0])
                logentry += channel[0] + ", "
            logentry = logentry[:-2] # hackertricks
            logging.info(logentry)
            if not channellist:
                # module table is empty
                raise Exception("channellist was empty")
            await self.join_channels(channellist)
        except:
            logging.error("could not extract channel list from DB on startup")
            logging.error(f"channellist:{channellist}")
            #try to create create the bots channel in module table
            logging.warning(f"trying to get my on channel into DB")
            self.DB_query(f"INSERT IGNORE INTO modules(channel) VALUES('{os.environ['TWITCH_BOT_USERNAME'].lower()}')")
            os._exit(1)
    
    async def event_message(self, ctx):
        # Runs every time a message is sent to the channel
        # ignore non existent author (twitchio bug):
        if ctx.author is None:
            return # this is a twitchio bug i guess, but it spamms my debug logs
        # ignore thyself
        if ctx.author.name.lower() == os.environ['TWITCH_BOT_USERNAME'].lower():
            logging.debug("own message detected and ignored")
            return

        # handle commands and evaluations
        await self.handle(ctx)