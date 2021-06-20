# local
from .Command import Command
from TTBot.data.MatchmakingData import MatchmakingData
from TTBot.logic.MatchmakingCache import MatchmakingCache
from TTBot.logic.TrackmaniaIO import TrackmaniaIO

class CommandMm(Command):
    pMatchmakingCache: MatchmakingCache
    pTrackmaniaIO: TrackmaniaIO
    
    @staticmethod
    def getCommandString() -> str:
        return 'mm'
    
    @staticmethod
    def getRightsId() -> str:
        return 'mm'
    
    def _buildFullMessage(self, matchmakingDataList: list) -> str:
        messages = [self._buildSingleMessage(pMatchmakingData) for pMatchmakingData in matchmakingDataList]
        return f"@{self.messageAuthor} {' | '.join(messages)}"
    # def _buildFullMessage(self, matchmakingDataList: list) -> str
    
    def _buildSingleMessage(self, pMatchmakingData: MatchmakingData) -> str:
        return f"#{pMatchmakingData.getRank()}: {pMatchmakingData.getPlayer()} ({pMatchmakingData.getScore()} points)"

    async def execute(self, args) -> str:
        playerNamePart = args[0]
        cachedData = self.pMatchmakingCache.get(playerNamePart)
        
        if cachedData:
            return self._buildFullMessage(cachedData)
        else:
            matchmakingData = self.pTrackmaniaIO.getMatchmakingData(playerNamePart)
            for pMatchmakingData in matchmakingData:
                self.pMatchmakingCache.write(pMatchmakingData)

            if matchmakingData:
                return self._buildFullMessage(matchmakingData)
            else:
                return f"@{self.messageAuthor} No player found in TM2020 matchmaking resembling the name '{playerNamePart}'!"
    # async def execute(self, args) -> str
# class CommandMm(Command)