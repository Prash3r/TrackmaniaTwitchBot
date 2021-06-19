# pylib
import datetime
import os
import requests

# local
from .Command import Command
from TTBot.logic.MariaDbWrapper import MariaDbWrapper

class CommandMm(Command):
    pMariaDbWrapper: MariaDbWrapper
    
    @staticmethod
    def getCommandString() -> str:
        return 'mm'
    
    @staticmethod
    def getRightsId() -> str:
        return 'mm'

    async def execute(self, args) -> str:
        user_agent = {'User-agent': os.environ['TMIO_USER_AGENT']} # ToDo needs testing
        #user_agent = {'User-agent': 'some fork of github.com/prash3r/TTBot - trackmania_bot - !mm command fetching outdated data'}
        result = False
        #clean = self.sanitize(args) needs to be sanitized somewhere else
        cur = self.pMariaDbWrapper.fetch(f"SELECT ranks_rank, ranks_displayname, ts, ranks_score FROM mmranking WHERE ranks_displayname = '{args[0]}';")
        for (ranks_rank, ranks_displayname, ts, ranks_score) in cur:
            # local results
            age = datetime.datetime.now() - ts
            ageminutes = int(age.total_seconds() / 60)
            if (((age < datetime.timedelta(minutes=ranks_rank)) or (age < datetime.timedelta(minutes=69))) and (age < datetime.timedelta(hours=12))) :
                # local data is fresh enough
                result = True
                return f"{ranks_displayname} is on rank {ranks_rank} ({ranks_score} points) (cached data {ageminutes}m old)"
        
        if not result:
            # hit the api
            urlproto = 'https://trackmania.io/api/players/find?search='
            url = urlproto + str(args[0])
            resp = requests.get(url=url, headers = user_agent)
            data = resp.json()
            #logging.info(data)
            writtentochat = 0
            msgstring = ""
            for player in data:
                if len(player['matchmaking']) == 0:
                    break
                result = True
                self.pMariaDbWrapper.query(f"REPLACE INTO mmranking (ranks_rank, ranks_score, ranks_displayname, ranks_accountid) \
                VALUES ('{player['matchmaking'][0]['rank']}', '{player['matchmaking'][0]['score']}', '{player['displayname']}', '{player['matchmaking'][0]['accountid']}');")
                if writtentochat < 3:
                    if writtentochat != 0 :
                        msgstring = msgstring + " | "
                    msgstring = msgstring + f"{player['displayname']} is on rank {player['matchmaking'][0]['rank']} ({player['matchmaking'][0]['score']} points)" 
                    #return f"{player['displayname']} is on rank {player['matchmaking'][0]['rank']} (fresh data)")
                    writtentochat = writtentochat + 1
            if not result:
                msgstring = f"There was no player found in Trackmania2020 resembling the name {args[0]}"
            return msgstring
    # async def execute(self, args) -> str
# class CommandMm(Command)