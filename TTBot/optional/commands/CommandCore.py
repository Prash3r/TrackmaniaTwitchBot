# local
from .Command import Command
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.MariaDbWrapper import MariaDbWrapper
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper

class CommandCore(Command):
    def getRightsId(self) -> str:
        return 'core'
# class CommandCore(Command)

class CommandUpdate(CommandCore):
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'update'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
            if messageAuthorName in ["axelalex2", "prash3r"]:
                from sys import exit
                exit()
            else:
                return f"@{messageAuthorName}, you cant make me do that"
        except Exception:
            return "going down failed miserably"
    # async def execute(self, pMessage, _) -> str
# class CommandUpdate(CommandCore)

class CommandInvite(CommandCore):
    pMariaDbWrapper: MariaDbWrapper
    pTwitchBotWrapper: TwitchBotWrapper
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'invite'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
            pTwitchBot = self.pTwitchBotWrapper.get()
            await pTwitchBot.join_channels([f'{messageAuthorName}'])

            self.pMariaDbWrapper.query(f"INSERT IGNORE INTO modules (channel) VALUES ('{messageAuthorName}');")
            return f"@{messageAuthorName} I joined your channel, now you can control me over there!"
        except:
            return "kem1W"
    # async def execute(self, pMessage, _) -> str
# class CommandInvite(CommandCore)

class CommandUninvite(CommandCore):
    pMariaDbWrapper: MariaDbWrapper
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'uninvite'
    
    async def execute(self, pMessage, _) -> str:
        try:
            messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
            self.pMariaDbWrapper.query(f"DELETE FROM modules WHERE channel = '{messageAuthorName}';")
            return f"@{messageAuthorName} I left your channel, you can reinvite me in my channel!"
        except:
            return "kem1W"
    # async def execute(self, pMessage, _) -> str
# class CommandUninvite(CommandCore)

class CommandModule(CommandCore):
    pInputSanitizer: InputSanitizer
    pMariaDbWrapper: MariaDbWrapper
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'module'
    
    def _activateModule(self, messageAuthorName, args: list) -> str:
        moduleName = args[0]
        hasMinimumUserLevel = len(args) >= 2 and self.pInputSanitizer.isInteger(args[1])
        minimumUserLevel = args[1] if hasMinimumUserLevel else 1

        self.pMariaDbWrapper.query(f"UPDATE modules SET `{moduleName}` = {minimumUserLevel} WHERE channel = '{messageAuthorName}';")
        return f"Module '{moduleName}' activated with access level {minimumUserLevel}!"
    # def _activateModule(self, args: list) -> str

    def _deactivateModule(self, messageAuthorName, moduleName: str) -> str:
        self.pMariaDbWrapper.query(f"UPDATE modules SET `{moduleName}` = 0 WHERE channel = '{messageAuthorName}';")
        return f"Module '{moduleName}' deactivated!"
    # def _deactivateModule(self, moduleName: str) -> str
    
    async def execute(self, pMessage, args: list) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        if len(args) > 0:
            arg = args[0].lower()
        else:
            arg = 'list'

        if arg == 'list':
            return f"@{messageAuthorName} {self._getModulesList(messageAuthorName)}"
        elif arg == 'add' and len(args) >= 2:
            return f"@{messageAuthorName} {self._activateModule(messageAuthorName, args[1:])}"
        elif arg == 'rem' and len(args) >= 2:
            return f"@{messageAuthorName} {self._deactivateModule(messageAuthorName, args[1])}"
        else:
            return "kem1W this one needs an argument"
    # async def execute(self, pMessage, args: list) -> str

    def _getModulesList(self, messageAuthorName: str) -> str:
        rows = self.pMariaDbWrapper.fetch(f"SELECT * FROM modules WHERE channel = '{messageAuthorName}' LIMIT 1;")
        if not rows:
            return "kem1W"
        
        output = []
        row = rows[0]
        for moduleName, userLevel in row.items():
            if moduleName in ['channel', 'ts']:
                continue

            output.append(f"{moduleName}: {userLevel}")
        # for moduleName, userLevel in row.items()

        return ', '.join(output)
    # def _getModulesList(self, messageAuthorName: str) -> str
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

    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'help'
    
    async def execute(self, pMessage, args: list) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)

        if args:
            return f"@{messageAuthorName} {self.HELP_MESSAGES.get(args[0], self.DEFAULT_HELP_MESSAGE)}"
                
        return f"@{messageAuthorName} {self.DEFAULT_HELP_MESSAGE}"
    # async def execute(self, pMessage, args: list) -> str
# class CommandHelp(CommandCore)