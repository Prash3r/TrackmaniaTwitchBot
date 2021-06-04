from twitchio.ext import commands
import requests
import datetime
import logging
import os

@commands.command(name='mm')
async def CMD_mm(self, ctx, args):
    if not self.rights(ctx, 'mm'):
        # maybe whisper that invoking person has no rights
        return
    logging.info(f"Command '!mm' running in channel '{ctx.channel.name}' invoked by user '{ctx.author.name}'")
    user_agent = {'User-agent': 'some fork of github.com/prash3r/TTBot - trackmania_bot - !mm command fetching outdated data'}
    result = False
    clean = self.sanitize(args)
    logging.info(f"the command !{ctx.command.full_name} had the arguments {ctx.args}")
    cur = self.DB_query(f"SELECT ranks_rank, ranks_displayname, ts, ranks_score FROM mmranking WHERE ranks_displayname = '{clean}';")
    for (ranks_rank, ranks_displayname, ts, ranks_score) in cur:
        # local results
        age = datetime.datetime.now() - ts
        ageminutes = int(age.total_seconds() / 60)
        if (((age < datetime.timedelta(minutes=ranks_rank)) or (age < datetime.timedelta(minutes=69))) and (age < datetime.timedelta(hours=12))) :
            # local data is fresh enough
            logging.info(f'data for {clean} is {ageminutes} minutes old -> good enough')
            result = True
            logging.info(f"{ranks_displayname} is on rank {ranks_rank}")
            await ctx.channel.send(f"{ranks_displayname} is on rank {ranks_rank} ({ranks_score} points) (cached data {ageminutes}m old)")
        else:
            logging.info(f'data for {clean} is {ageminutes} minutes old -> i will fetch new data')
    if result == False :
        # hit the api
        urlproto = 'https://trackmania.io/api/players/find?search='
        logging.info(f"fetching data from trackmania.io api for player {clean}")
        url = urlproto + str(clean)
        resp = requests.get(url=url, headers = user_agent)
        data = resp.json()
        #logging.info(data)
        writtentochat = 0
        msgstring = ""
        for player in data:
            if len(player['matchmaking']) == 0:
                break
            result = True
            cur.execute(f"REPLACE INTO mmranking (ranks_rank, ranks_score, ranks_displayname, ranks_accountid) \
            VALUES ('{player['matchmaking'][0]['rank']}', '{player['matchmaking'][0]['score']}', '{player['displayname']}', '{player['matchmaking'][0]['accountid']}');")
            if writtentochat < 3:
                if writtentochat != 0 :
                    msgstring = msgstring + " | "
                msgstring = msgstring + f"{player['displayname']} is on rank {player['matchmaking'][0]['rank']} ({player['matchmaking'][0]['score']} points)" 
                #await ctx.channel.send(f"{player['displayname']} is on rank {player['matchmaking'][0]['rank']} (fresh data)")
                writtentochat = writtentochat + 1
        if result == False:
            msgstring = f"There was no player found in Trackmania2020 resembling the name {clean}"
        await ctx.channel.send(msgstring)