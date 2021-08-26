# vendor
import minidi

# local
from TTBot.data.MatchmakingData import MatchmakingData

class MatchmakingDataFactory(minidi.Injectable):
	def createFromCacheQuery(self, cacheData: list) -> MatchmakingData:
		pMatchmakingData = MatchmakingData()
		pMatchmakingData.setPlayer(cacheData['ranks_displayname'])
		pMatchmakingData.setRank(cacheData['ranks_rank'])
		pMatchmakingData.setScore(cacheData['ranks_score'])
		pMatchmakingData.setTimestamp(cacheData['ts'])
		return pMatchmakingData
	# def createFromCacheQuery(self, cacheData: list) -> MatchmakingData

	def createFromTrackmaniaIO(self, tmIoData: dict) -> MatchmakingData:
		pMatchmakingData = MatchmakingData()
		pMatchmakingData.setPlayer(tmIoData['player']['name'])
		pMatchmakingData.setRank(tmIoData['matchmaking'][0]['rank'])
		pMatchmakingData.setScore(tmIoData['matchmaking'][0]['score'])
		pMatchmakingData.setPlayerAccountId(tmIoData['matchmaking'][0]['accountid'])
		return pMatchmakingData
	# def createFromTrackmaniaIO(self, tmIoData: dict) -> MatchmakingData
# class MatchmakingDataFactory(minidi.Injectable)