# vendor
import minidi
from TTBot.logic.InputSanitizer import InputSanitizer
from twitchio.ext import commands

# local
from .Command import Command

class CommandCore(Command):
    pTwitchBot : commands.Bot
    funcDB_query : callable
    pctx : any

    @staticmethod
    def getRightsId() -> str:
        return 'core'

class CommandInvite(CommandCore):    
    @staticmethod
    def getCommandString() -> str:
        return 'invite'
    
    async def execute(self, args) -> str:
        try:
            await self.pTwitchBot.join_channels([f'{self.messageAuthor}'])
            self.funcDB_query(f"INSERT IGNORE INTO modules(channel) VALUES('{self.messageAuthor}')")
            #await self.pTwitchBot.get_channel(self.messageAuthor).send(f'/me coming in hot') # i have no idea why this doesnt work
            #await self.pctx.channel.send(f'I joined your channel, {self.messageAuthor}. You can only control me over there')
            return f'I joined your channel, {self.messageAuthor}. You can only control me over there'
        except:
            return 'kem1W'

class CommandUninvite(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'uninvite'
    
    async def execute(self, args) -> str:
        try:
            self.funcDB_query(f"DELETE FROM modules WHERE channel='{self.messageAuthor}'")
            # i know, this is bad, but for some reason i cant find the proper leave command from twitchio
            #await ctx.channel.send(f'I am leaving your channel right now, {self.messageAuthor}. You can invite me in my channel again')
            #await self.pTwitchBot.part_channels(self.messageAuthor) # ToDo this doesnt exist - will not join after restart thou.
            return f'I wont join your channel anymore, {self.messageAuthor}. You can invite me in my channel again'
        except:
            return 'kem1W'

class CommandModule(CommandCore):
    @staticmethod
    def getCommandString() -> str:
        return 'module'
    
    async def execute(self, args) -> str:
        try:
            if args[0].lower() == 'list':
                cur = self.funcDB_query(f"SELECT luckerscounter, joke, kem, mm, roll, score, ooga, ping, test FROM modules WHERE channel = '{self.messageAuthor}'")
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
            #elif ((args[1] not in self.modules) or (len(self.messageAuthor)<2)):
            #    return # short names shouldnt happen and this way i dont need a list containing all active modules
            else:
                if args[0].lower() == 'add':
                    if (len(args) == 3):
                        pInputSanitizer: InputSanitizer = minidi.get(InputSanitizer)
                        if pInputSanitizer.isInteger(args[2]):
                            self.funcDB_query(f"UPDATE modules SET {args[1]}={args[2]} WHERE channel='{self.messageAuthor}'")
                            return f'module {args[1]} added to your channel {self.messageAuthor} with access level {args[2]}'
                    else:
                        self.funcDB_query(f"UPDATE modules SET {args[1]}=1 WHERE channel='{self.messageAuthor}'")
                        return f'module {args[1]} added to your channel {self.messageAuthor} for everyone to use'
                    pass
                elif args[0].lower() == 'rem':
                    self.funcDB_query(f"UPDATE modules SET {args[1]}=0 WHERE channel='{self.messageAuthor}'")
                    return f'module {args[1]} removed from your channel, {self.messageAuthor}'
        except:
            return 'kem1W'

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