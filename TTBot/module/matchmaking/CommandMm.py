# local
from TTBot.data.Message import Message
from TTBot.module.matchmaking.MatchmakingCache import MatchmakingCache
from TTBot.module.matchmaking.MatchmakingData import MatchmakingData
from TTBot.module.matchmaking.TrackmaniaIoMatchmaking import TrackmaniaIoMatchmaking
from TTBot.module.Command import Command

class CommandMm(Command):
    pMatchmakingCache: MatchmakingCache
    pTrackmaniaIoMatchmaking: TrackmaniaIoMatchmaking
    
    def getCommandTrigger(self):
        return ['matchmaking', 'mm']
    
    def getModuleId(self) -> str:
        return 'mm'
    
    def _buildFullMessage(self, matchmakingDataList: list) -> str:
        messages = []
        results = 0
        for pMatchmakingData in matchmakingDataList:
            messages.append(self._buildSingleMessage(pMatchmakingData))
            results += 1
            if results > 4:
                messages.append("and more")
                break
        return ' | '.join(messages)
        # the following was spamming a little bit since we split messages into multiple chat msg when the char limit is reached.
        # messages = [self._buildSingleMessage(pMatchmakingData) for pMatchmakingData in matchmakingDataList]
        # return ' | '.join(messages)
    # def _buildFullMessage(self, matchmakingDataList: list) -> str
    
    def _buildSingleMessage(self, pMatchmakingData: MatchmakingData) -> str:
        return f"#{pMatchmakingData.getRank()}: {pMatchmakingData.getPlayer()} ({pMatchmakingData.getScore()} points)"

    async def execute(self, pMessage: Message, args: list) -> str:
        messageAuthorName = pMessage.getAuthor().getName()

        if not args:
            return f"@{messageAuthorName} Missing a player name (or part of a players name)!"

        playerNamePart = args[0]
        cachedData = self.pMatchmakingCache.get(playerNamePart)
        
        if cachedData:
            return f"@{messageAuthorName} {self._buildFullMessage(cachedData)}"
        else:
            matchmakingData = self.pTrackmaniaIoMatchmaking.getMatchmakingData(playerNamePart)
            for pMatchmakingData in matchmakingData:
                self.pMatchmakingCache.write(pMatchmakingData)

            if matchmakingData:
                return f"@{messageAuthorName} {self._buildFullMessage(matchmakingData)}"
            else:
                return f"@{messageAuthorName} No player found in TM2020 matchmaking resembling the name '{playerNamePart}'!"
    # async def execute(self, pMessage: Message, args: list) -> str
# class CommandMm(Command)