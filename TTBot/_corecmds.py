import twitchio
from twitchio.ext import commands
import random
import os
import time
import logging


@commands.command(name='invite')
async def CMD_invite(self, ctx):
    try:
        if self.botchathome(ctx):
            # invite is only possible in ther bots chatroom
            # ToDo: Check if channel is in Database-channellist
            # ToDo: if not add channel to channel list
            # ToDo: if user not in userlist create user with default settings
            # join channel:
            await self.join_channels([f'{str(ctx.author.name)}'])
            logging.info(f"Bot was invited to the channel '{ctx.author.name}'.")
            await ctx.channel.send(f'I joined your channel, {ctx.author.name}. You can only control me over there')
            self.DB_query(f"INSERT IGNORE INTO modules(channel) VALUES('{ctx.author.name}')")
            await self.get_channel(str(ctx.author.name)).send(f'/me coming in hot')
    except:
        pass

@commands.command(name='uninvite')
async def CMD_uninvite(self, ctx):
    if self.ownerrights(ctx) or self.botchathome(ctx):
        self.DB_query(f"DELETE FROM modules WHERE channel='{ctx.author.name}'")
        logging.info(f"Bot was uninvited from the channel '{ctx.author.name}'.")
        # i know, this is bad, but for some reason i cant find the proper leave command from twitchio
        #await ctx.channel.send(f'I am leaving your channel right now, {ctx.author.name}. You can invite me in my channel again')
        await ctx.channel.send(f'I wont join your channel anymore, {ctx.author.name}. You can invite me in my channel again')
        await self.part_channels(ctx.author.name) # ToDo this doesnt exist - will not join after restart thou.

@commands.command(name='module')
async def CMD_module(self, ctx, *args):
    try:
        if self.ownerrights(ctx) or self.botchathome(ctx):
            if args[0].lower() == 'list':
                cur = self.DB_query(f"SELECT luckerscounter, joke, kem, mm, roll, score, ooga, ping, test FROM modules WHERE channel = '{ctx.author.name}'")
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
                await ctx.channel.send(f'{reply}{ctx.author.name}')
            #elif ((args[1] not in self.modules) or (len(ctx.author.name)<2)):
            #    return # short names shouldnt happen and this way i dont need a list containing all active modules
            else:
                if args[0].lower() == 'add':
                    if (len(args) == 3):
                        if self.isint(args[2]):
                            self.DB_query(f"UPDATE modules SET {args[1]}={args[2]} WHERE channel='{ctx.author.name}'")
                            logging.info(f"module {args[1]} added the channel '{ctx.author.name}' with access level '{args[2]}'")
                            await ctx.channel.send(f'module {args[1]} added to your channel {ctx.author.name} with access level {args[2]}')
                    else:
                        self.DB_query(f"UPDATE modules SET {args[1]}=1 WHERE channel='{ctx.author.name}'")
                        logging.info(f"module {args[1]} added the channel '{ctx.author.name}' for everyone to use")
                        await ctx.channel.send(f'module {args[1]} added to your channel {ctx.author.name} for everyone to use')
                    pass
                elif args[0].lower() == 'rem':
                    self.DB_query(f"UPDATE modules SET {args[1]}=0 WHERE channel='{ctx.author.name}'")
                    logging.info(f"module {args[1]} removed from the channel '{ctx.author.name}'")
                    await ctx.channel.send(f'module {args[1]} removed from your channel, {ctx.author.name}')                        
    except Exception as e:
        logging.error(e)

@commands.command(name='test')
async def CMD_test(self, ctx):
    if ctx.author.name == "prash3r":
        await ctx.channel.send('kem1W')

@commands.command(name='help')
async def CMD_help(self, ctx, args=""):
    if ((ctx.channel.name.lower() != ctx.author.name.lower()) and (ctx.channel.name.lower() !=os.environ['TWITCH_BOT_USERNAME'])):
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

