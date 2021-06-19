# vendor
import minidi
import twitchio

# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.MariaDbWrapper import MariaDbWrapper

class CommandCore(Command):
    pMariaDbWrapper: MariaDbWrapper
    pMessage: twitchio.Message
    pTwitchBot: twitchio.ext.commands.Bot

    @staticmethod
    def getRightsId() -> str:
        return 'core'
# class CommandCore(Command)

class CommandInvite(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'invite'
    
    async def execute(self, args) -> str:
        try:
            await self.pTwitchBot.join_channels([f'{self.messageAuthor}'])

            self.pMariaDbWrapper.query(f"INSERT IGNORE INTO modules (channel) VALUES ('{self.messageAuthor}');")
            return f"@{self.messageAuthor} I joined your channel, now you can control me over there!"
        except:
            return "kem1W"
# class CommandInvite(CommandCore)

class CommandUninvite(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'uninvite'
    
    async def execute(self, args) -> str:
        try:
            self.pMariaDbWrapper.query(f"DELETE FROM modules WHERE channel = '{self.messageAuthor}';")
            return f"@{self.messageAuthor} I left your channel, you can reinvite me in my channel!"
        except:
            return "kem1W"
# class CommandUninvite(CommandCore)

class CommandModule(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'module'
    
    def _activateModule(self, args: list) -> str:
        pInputSanitizer: InputSanitizer = minidi.get(InputSanitizer)

        moduleName = args[0]
        hasMinimumUserLevel = len(args) >= 2 and pInputSanitizer.isInteger(args[1])
        minimumUserLevel = args[1] if hasMinimumUserLevel else 1

        self.pMariaDbWrapper.query(f"UPDATE modules SET `{moduleName}` = {minimumUserLevel} WHERE channel = '{self.messageAuthor}';")
        return f"@{self.messageAuthor} Module '{moduleName}' activated with access level {minimumUserLevel}!"
    # def _activateModule(self, args: list) -> str

    def _deactivateModule(self, moduleName: str) -> str:
        self.pMariaDbWrapper.query(f"UPDATE modules SET `{moduleName}` = 0 WHERE channel = '{self.messageAuthor}';")
        return f"@{self.messageAuthor} Module '{moduleName}'' deactivated!"
    # def _deactivateModule(self, moduleName: str) -> str
    
    async def execute(self, args: list) -> str:
        arg = args[0].lower()

        if arg == 'list':
            return self._getModulesList()
        elif arg == 'add' and len(args) >= 2:
            return self._activateModule(args[1:])
        elif arg == 'rem' and len(args) >= 2:
            return self._deactivateModule(args[1])
        else:
            return "kem1W"
    # async def execute(self, args: list) -> str

    def _getModulesList(self) -> str:
        rows = self.pMariaDbWrapper.fetch(f"SELECT luckerscounter, joke, kem, mm, roll, score, ooga, ping, test FROM modules WHERE channel = '{self.messageAuthor}' LIMIT 1;")
        if not rows:
            return "kem1W"
        
        row = rows[0]
        moduleAccessLevelList = [
            f"luckerscounter:{row[0]}",
            f"joke:{row[1]}",
            f"kem:{row[2]}",
            f"mm:{row[3]}",
            f"roll:{row[4]}",
            f"score:{row[5]}",
            f"ooga:{row[6]}",
            f"ping:{row[7]}",
            f"test:{row[8]}",
        ]

        return f"@{self.messageAuthor} module:accesslevel - {', '.join(moduleAccessLevelList)}"
    # def _getModulesList(self) -> str
# class CommandModule(CommandCore)

class CommandHelp(CommandCore):
    DEFAULT_HELP_MESSAGE = "Use '!help invite/uninvite/accesslevel/add/list/rem' for detailed information about this bots core commands!"
    HELP_MESSAGES = {
        'invite': "Use the command '!invite' to invite this bot to your channel!",
        'uninvite': "Use the command '!uninvite' to make the bot leave your channel!",
        'accesslevel': "Use the command '!module add modulename 10' to enable a module on your channel with a minimum access level required!",
        'add': "Use the command '!module add modulename' to enable a module on your channel for everyone!",
        'list': "Use the command '!module list' to view the enabled modules on your channel!",
        'rem': "Use the command '!module rem' to disable the module on your channel!"
    }

    @staticmethod
    def getCommandString() -> str:
        return 'help'
    
    async def execute(self, args: list) -> str:
        if args:
            return self.HELP_MESSAGES.get(args[0], self.DEFAULT_HELP_MESSAGE)
        
        return self.DEFAULT_HELP_MESSAGE
    # async def execute(self, args: list) -> str
# class CommandHelp(CommandCore)