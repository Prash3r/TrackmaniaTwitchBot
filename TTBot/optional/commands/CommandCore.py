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

            self.pMariaDbWrapper.query(f"INSERT IGNORE INTO modules(channel) VALUES('{self.messageAuthor}')")
            return f'I joined your channel, {self.messageAuthor}, now you can control me over there.'
        except:
            return 'kem1W'
# class CommandInvite(CommandCore)

class CommandUninvite(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'uninvite'
    
    async def execute(self, args) -> str:
        try:
            self.pMariaDbWrapper.query(f"DELETE FROM modules WHERE channel='{self.messageAuthor}'")
            return f'I left your channel, {self.messageAuthor}, you can reinvite me in my channel!'
        except:
            return 'kem1W'
# class CommandUninvite(CommandCore)

class CommandModule(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'module'
    
    async def execute(self, args) -> str:
        try:
            if args[0].lower() == 'list':
                cur = self.pMariaDbWrapper.fetch(f"SELECT luckerscounter, joke, kem, mm, roll, score, ooga, ping, test FROM modules WHERE channel = '{self.messageAuthor}'")
                #following should be reworked more diynamically and not at all hardcoded:
                reply = "module:accesslevel - "
                for (luckerscounter, joke, kem, mm, roll, score, ooga, ping, test) in cur:
                    reply += f"luckerscounter:{luckerscounter}, "
                    reply += f"joke:{joke}, "
                    reply += f"kem:{kem}, "
                    reply += f"mm:{mm}, "
                    reply += f"roll:{roll}, "
                    reply += f"score:{score}, "
                    reply += f"ooga:{ooga}, "
                    reply += f"ping:{ping}, "
                    reply += f"test:{test}, "
                # maybe put the evaluation above into the config.py file.
                return f'{reply}{self.messageAuthor}'
            else:
                if args[0].lower() == 'add':
                    if (len(args) == 3):
                        pInputSanitizer: InputSanitizer = minidi.get(InputSanitizer)
                        if pInputSanitizer.isInteger(args[2]):
                            self.pMariaDbWrapper.query(f"UPDATE modules SET {args[1]}={args[2]} WHERE channel='{self.messageAuthor}'")
                            return f'module {args[1]} added to your channel {self.messageAuthor} with access level {args[2]}'
                    else:
                        self.pMariaDbWrapper.query(f"UPDATE modules SET {args[1]}=1 WHERE channel='{self.messageAuthor}'")
                        return f'module {args[1]} added to your channel {self.messageAuthor} for everyone to use'
                    pass
                elif args[0].lower() == 'rem':
                    self.pMariaDbWrapper.query(f"UPDATE modules SET {args[1]}=0 WHERE channel='{self.messageAuthor}'")
                    return f'module {args[1]} removed from your channel, {self.messageAuthor}'
        except:
            return 'kem1W'
# class CommandModule(CommandCore)

class CommandHelp(CommandCore):    
    @staticmethod
    def getCommandString() -> str:
        return 'help'
    
    async def execute(self, args) -> str:
        try:
            if ("invite" in args):
                return "use the command '!invite' to invite this bot to your channel"
            elif ("uninvite" in args):
                return "use the command '!uninvite' to make the bot leave your channel"
            elif ("module" in args):
                return "use the command '!module list' see the currently loaded modules (future feature)"
            elif ("add" in args):
                return "use the command '!module add modulename' to add the named module to your channel"
            elif ("rem" in args):
                return "use the command '!module rem modulename' remove the named module from your channel"
            elif ("accesslevel" in args):
                return "use the command '!module add modulename 10' to make the module available for moderators only"
            else:
                return "you can request help for the following topics !help invite/uninvite/module/add/remove/accesslevel"
        except:
            return 'kem1W'
# class CommandHelp(CommandCore)