# pylib
#import time
import random
# local
from twitchio.ext import commands
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
                        if self.isint(args[2]):
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



    

'''

import twitchio
from twitchio.ext import commands
import random
import os
import time
import logging




async def CommandInvite(self, ctx):
    

@commands.command(name='uninvite')
async def CMD_uninvite(self, ctx):
    if self.ownerrights(ctx) or self.botchathome(ctx):
        self.funcDB_query(f"DELETE FROM modules WHERE channel='{self.messageAuthor}'")
        logging.info(f"Bot was uninvited from the channel '{self.messageAuthor}'.")
        # i know, this is bad, but for some reason i cant find the proper leave command from twitchio
        #await ctx.channel.send(f'I am leaving your channel right now, {self.messageAuthor}. You can invite me in my channel again')
        await ctx.channel.send(f'I wont join your channel anymore, {self.messageAuthor}. You can invite me in my channel again')
        await self.part_channels(self.messageAuthor) # ToDo this doesnt exist - will not join after restart thou.

@commands.command(name='module')
async def CMD_module(self, ctx, *args):
    try:
        if self.ownerrights(ctx) or self.botchathome(ctx):
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
                await ctx.channel.send(f'{reply}{self.messageAuthor}')
            #elif ((args[1] not in self.modules) or (len(self.messageAuthor)<2)):
            #    return # short names shouldnt happen and this way i dont need a list containing all active modules
            else:
                if args[0].lower() == 'add':
                    if (len(args) == 3):
                        if self.isint(args[2]):
                            self.funcDB_query(f"UPDATE modules SET {args[1]}={args[2]} WHERE channel='{self.messageAuthor}'")
                            logging.info(f"module {args[1]} added the channel '{self.messageAuthor}' with access level '{args[2]}'")
                            await ctx.channel.send(f'module {args[1]} added to your channel {self.messageAuthor} with access level {args[2]}')
                    else:
                        self.funcDB_query(f"UPDATE modules SET {args[1]}=1 WHERE channel='{self.messageAuthor}'")
                        logging.info(f"module {args[1]} added the channel '{self.messageAuthor}' for everyone to use")
                        await ctx.channel.send(f'module {args[1]} added to your channel {self.messageAuthor} for everyone to use')
                    pass
                elif args[0].lower() == 'rem':
                    self.funcDB_query(f"UPDATE modules SET {args[1]}=0 WHERE channel='{self.messageAuthor}'")
                    logging.info(f"module {args[1]} removed from the channel '{self.messageAuthor}'")
                    await ctx.channel.send(f'module {args[1]} removed from your channel, {self.messageAuthor}')                        
    except Exception as e:
        logging.error(e)

@commands.command(name='test')
async def CMD_test(self, ctx):
    if self.messageAuthor == "prash3r":
        await ctx.channel.send('kem1W')

@commands.command(name='help')
async def CMD_help(self, ctx, args=""):
    if ((ctx.channel.name.lower() != self.messageAuthor.lower()) and (ctx.channel.name.lower() !=os.environ['TWITCH_BOT_USERNAME'])):
        return
    try:
        if ("invite" in args):
            await ctx.channel.send("use the command '!invite' to invite this bot to your channel")
        elif ("uninvite" in args):
            await ctx.channel.send("use the command '!uninvite' to make the bot leave your channel")
        elif ("module" in args):
            await ctx.channel.send("use the command '!module list' see the currently loaded modules (future feature)")
        elif ("add" in args):
            await ctx.channel.send("use the command '!module add modulename' to add the named module to your channel")
        elif ("rem" in args):
            await ctx.channel.send("use the command '!module rem modulename' remove the named module from your channel")
        elif ("accesslevel" in args):
            await ctx.channel.send("use the command '!module add modulename 10' to make the module available for moderators only")
        else:
            await ctx.channel.send("you can request help for the following topics !help invite/uninvite/module/add/remove/accesslevel")
    except:
        pass



'''