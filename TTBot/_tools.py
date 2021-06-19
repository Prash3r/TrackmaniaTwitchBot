# vendor
import minidi

# local
from .logic.TwitchMessageEvaluator import TwitchMessageEvaluator

def isint(self, s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def rights(self, ctx, command):
    # ONLY for dynamically choosable commands. rights for basic commands are handled individually in their own functions
    try:
        pTwitchMessageEvaluator: TwitchMessageEvaluator = minidi.get(TwitchMessageEvaluator)
        if command == 'core' and (pTwitchMessageEvaluator.isOwnerMessage(ctx) or pTwitchMessageEvaluator.isBotChannel(ctx)):
            return True
        
        channelName = pTwitchMessageEvaluator.getChannelName(ctx)
        # ToDo: what happens if args[0] doesnt exist or its not a viable column in the table?
        # get user lvl of command in this channel and check if the user fits the requirements
        # completely untested, this should not work yet:
        cur = self.DB_query(f"SELECT {command} FROM modules WHERE channel = '{channelName.lower()}' LIMIT 1")
        for accessLevel in cur:
            if accessLevel[0] == None:
                return False
            elif accessLevel[0] == 0:
                return False
            else:
                return accessLevel[0] <= pTwitchMessageEvaluator.getUserLevel(ctx)
        return False
    except:
        return False