# vendor
import minidi

# local
from TTBot.data.MatchmakingData import MatchmakingData
from .DateTimeChecker import DateTimeChecker
from .MariaDbWrapper import MariaDbWrapper
from .MatchmakingDataFactory import MatchmakingDataFactory

class MatchmakingCache(minidi.Injectable):
	pDateTimeChecker: DateTimeChecker
	pMariaDbWrapper: MariaDbWrapper
	pMatchmakingDataFactory: MatchmakingDataFactory

	def get(self, playerLoginPart: str) -> list:
		"""Gets MatchmakingData from the cache with the following logic:
		- if player is rank < 69 -> use max. 69 minutes old cache data
		- if player is rank >= 69 -> use 'rank' minutes old cache data
		- if cache data is >= 12 hours old -> don't use cache data"""

		rows = self.pMariaDbWrapper.fetch(f"SELECT ranks_rank, ranks_displayname, ts, ranks_score FROM mmranking WHERE ranks_displayname = '{playerLoginPart}';")

		if not rows:
			return False

		cachedData = []

		for row in rows:
			pMatchmakingData = self.pMatchmakingDataFactory.createFromCacheQuery(row)
			pTimestamp = pMatchmakingData.getTimestamp()
			pAge = self.pDateTimeChecker.getTimestampAge(pTimestamp)

			isYoungerThanRank    = self.pDateTimeChecker.isYoungerThan(pAge, minutes=pMatchmakingData.getRank())
			isYoungerThanNice    = self.pDateTimeChecker.isYoungerThan(pAge, minutes=69)
			isYoungerThanHalfDay = self.pDateTimeChecker.isYoungerThan(pAge, hours=12)

			if isYoungerThanHalfDay and (isYoungerThanRank or isYoungerThanNice):
				cachedData.append(pMatchmakingData)
		
		return cachedData
	# def get(self, playerLoginPart: str) -> list

	def write(self, pMatchmakingData: MatchmakingData) -> bool:
		rowsAffected = self.pMariaDbWrapper.query(f"REPLACE INTO mmranking (ranks_rank, ranks_score, ranks_displayname, ranks_accountid) \
		VALUES ('{pMatchmakingData.getRank()}', '{pMatchmakingData.getScore()}', '{pMatchmakingData.getPlayer()}', '{pMatchmakingData.getPlayerAccountId()}');")

		return rowsAffected == 1
	# def write(self, pMatchmakingData: MatchmakingData) -> bool
# class MatchmakingCache(minidi.Injectable)