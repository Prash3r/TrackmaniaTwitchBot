# vendor
import minidi

# local
from TTBot.data.MatchmakingData import MatchmakingData

class MatchmakingDataFactory(minidi.Injectable):
	def createFromCacheQuery(self, cacheData: list) -> MatchmakingData:
		pMatchmakingData = MatchmakingData()
		pMatchmakingData.setPlayer(cacheData[1])
		pMatchmakingData.setRank(cacheData[0])
		pMatchmakingData.setScore(cacheData[3])
		pMatchmakingData.setTimestamp(cacheData[2])
		return pMatchmakingData
	# def createFromCacheQuery(self, cacheData: list) -> MatchmakingData

	def createFromTrackmaniaIO(self, cacheData: dict) -> MatchmakingData:
		pMatchmakingData = MatchmakingData()
		pMatchmakingData.setPlayer(cacheData['displayname'])
		pMatchmakingData.setRank(cacheData['matchmaking'][0]['rank'])
		pMatchmakingData.setScore(cacheData['matchmaking'][0]['score'])
		pMatchmakingData.setPlayerAccountId(cacheData['matchmaking'][0]['accountid'])
		return pMatchmakingData
	# def createFromTrackmaniaIO(self, cacheData: dict) -> MatchmakingData
# class MatchmakingDataFactory(minidi.Injectable)