# vendor
import minidi

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.module.cotd.CotdInfo import CotdInfo
from TTBot.module.cotd.CotdInfoFactory import CotdInfoFactory

class CotdInfoCache(minidi.Injectable):
	pCotdInfoFactory: CotdInfoFactory
	pDbConnector: DbConnector

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `cotd_info` ( \
			`id` INT NOT NULL, \
			`name` VARCHAR(255) NOT NULL, \
			`num_players` INT NOT NULL, \
			`date_start` TIMESTAMP NOT NULL, \
			`date_end` TIMESTAMP NOT NULL, \
			`winner` VARCHAR(255), \
			PRIMARY KEY  (`id`) \
		);"

		self.pDbConnector.execute(query)
	# def afterInit(self)

	def getIdsWithWinner(self, limit: int) -> list[int]:
		query = "SELECT `id` \
			FROM `cotd_info` \
			WHERE `winner` IS NOT NULL \
			ORDER BY `date_end` DESC \
			LIMIT ?;"
		
		rows = self.pDbConnector.fetch(query, [limit])
		return [row['id'] for row in rows]
	# def getIdsWithWinner(self, limit: int) -> list[int]

	def getNext(self) -> CotdInfo:
		query = "SELECT * \
			FROM `cotd_info` \
			WHERE `winner` IS NULL \
			ORDER BY `date_start` ASC \
			LIMIT 1;"
		
		rows = self.pDbConnector.fetch(query)

		if not rows:
			return False
		
		return self.pCotdInfoFactory.createFromCacheQuery(rows[0])
	# def getNext(self) -> CotdInfo

	def getPrev(self) -> CotdInfo:
		query = "SELECT * \
			FROM `cotd_info` \
			WHERE `winner` IS NOT NULL \
			ORDER BY `date_end` DESC \
			LIMIT 1;"
		rows = self.pDbConnector.fetch(query)

		if not rows:
			return False
		
		return self.pCotdInfoFactory.createFromCacheQuery(rows[0])
	# def getPrev(self) -> CotdInfo

	def write(self, pCotdInfo: CotdInfo) -> bool:
		query = f"REPLACE INTO `cotd_info` \
			(`id`, `name`, `num_players`, `date_start`, `date_end`, `winner`) \
			VALUES (?, ?, ?, ?, ?, ?);"
		
		inputs = [
			pCotdInfo.getId(),
			pCotdInfo.getName(),
			pCotdInfo.getNumPlayers(),
			pCotdInfo.getDateStart(),
			pCotdInfo.getDateEnd(),
			pCotdInfo.getWinner()
		]
		
		rowsAffected = self.pDbConnector.execute(query, inputs)
		return rowsAffected == 1
	# def write(self, pCotdInfo: CotdInfo) -> bool
# class CotdInfoCache(minidi.Injectable)