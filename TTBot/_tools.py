import re
import os
'''
remove some characters from arguments provided by the user
'''
def sanitize(self, dirty):
    return re.sub('[!@#$\'%´`"]', '', dirty)

def ownerrights(self, ctx):
    try:
        return (ctx.channel.name.lower() == ctx.author.name.lower())
    except:
        return False

def botchathome(self, ctx):
    try:
        return (ctx.channel.name.lower() == os.environ['TWITCH_BOT_USERNAME'].lower())
    except:
        return False

def isint(self, s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def getUserLevel(self, ctx):
    try:
        if ((ctx.author.name.lower() == 'prash3r') or ((ctx.author.name.lower() == ctx.channel.name.lower()))):
            return 100
        elif (ctx.author.is_mod()):
            return 10
        elif (ctx.author.is_subscriber()):
            return 5
        else:
            return 1
    except:
        return 1

def rights(self, ctx, command):
    # ONLY for dynamically choosable commands. rights for basic commands are handled individually in their own functions
    try:
        if ((command == 'core') and ((ctx.channel.name == ctx.author.name) or (botchathome(self, ctx)))):
            return True
        # ToDo: what happens if args[0] doesnt exist or its not a viable column in the table?
        # get user lvl of command in this channel and check if the user fits the requirements
        # completely untested, this should not work yet:
        cur = self.DB_query(f"SELECT {command} FROM modules WHERE channel = '{ctx.channel.name.lower()}' LIMIT 1")
        for (accessLevel) in cur:
            if accessLevel[0] == None:
                return False
            elif accessLevel[0] == 0:
                return False
            else:
                return accessLevel[0] <= self.getUserLevel(ctx)
        return False
    except:
        return False