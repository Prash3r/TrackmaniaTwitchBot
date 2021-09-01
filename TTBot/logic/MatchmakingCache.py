# vendor
import minidi

# local
from TTBot.data.MatchmakingData import MatchmakingData
from .DateTimeChecker import DateTimeChecker
from .DbConnector import DbConnector
from .MatchmakingDataFactory import MatchmakingDataFactory

class MatchmakingCache(minidi.Injectable):
	pDateTimeChecker: DateTimeChecker
	pDbConnector: DbConnector
	pMatchmakingDataFactory: MatchmakingDataFactory

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `mmranking` (\
			`ranks_rank` INT,\
			`ranks_score` INT,\
			`ranks_division_position` INT,\
			`ranks_division_rule` VARCHAR(12) CHARACTER SET utf8,\
			`ranks_division_minpoints` INT,\
			`ranks_division_maxpoints` INT,\
			`ranks_displayname` VARCHAR(50) CHARACTER SET utf8,\
			`ranks_accountid` VARCHAR(36) CHARACTER SET utf8,\
			`ranks_zone_name` VARCHAR(28) CHARACTER SET utf8,\
			`ranks_zone_flag` VARCHAR(28) CHARACTER SET utf8,\
			`ranks_zone_parent_name` VARCHAR(23) CHARACTER SET utf8,\
			`ranks_zone_parent_flag` VARCHAR(23) CHARACTER SET utf8,\
			`ranks_zone_parent_parent_name` VARCHAR(13) CHARACTER SET utf8,\
			`ranks_zone_parent_parent_flag` VARCHAR(8) CHARACTER SET utf8,\
			`ranks_zone_parent_parent_parent_name` VARCHAR(6) CHARACTER SET utf8,\
			`ranks_zone_parent_parent_parent_flag` VARCHAR(6) CHARACTER SET utf8,\
			`ranks_zone_parent_parent_parent_parent_name` VARCHAR(5) CHARACTER SET utf8,\
			`ranks_zone_parent_parent_parent_parent_flag` VARCHAR(3) CHARACTER SET utf8,\
			`page` INT,\
			`note` INT,\
			`ts` TIMESTAMP,\
			PRIMARY KEY USING BTREE (`ranks_accountid`)\
		);"
		
		self.pDbConnector.execute(query)
	# def afterInit(self)

	def get(self, playerLoginPart: str) -> list:
		"""Gets MatchmakingData from the cache with the following logic:
		- if player is rank < 69 -> use max. 69 minutes old cache data
		- if player is rank >= 69 -> use 'rank' minutes old cache data
		- if cache data is >= 12 hours old -> don't use cache data"""

		rows = self.pDbConnector.fetch(f"SELECT ranks_rank, ranks_displayname, ts, ranks_score FROM mmranking WHERE ranks_displayname = '{playerLoginPart}';")

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
		# for row in rows
		
		return cachedData
	# def get(self, playerLoginPart: str) -> list

	def write(self, pMatchmakingData: MatchmakingData) -> bool:
		rowsAffected = self.pDbConnector.execute(f"REPLACE INTO mmranking (ranks_rank, ranks_score, ranks_displayname, ranks_accountid) \
		VALUES ('{pMatchmakingData.getRank()}', '{pMatchmakingData.getScore()}', '{pMatchmakingData.getPlayer()}', '{pMatchmakingData.getPlayerAccountId()}');")

		return rowsAffected == 1
	# def write(self, pMatchmakingData: MatchmakingData) -> bool
# class MatchmakingCache(minidi.Injectable)