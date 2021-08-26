# vendor
import mariadb
import minidi

# local
from .Environment import Environment
from .InputSanitizer import InputSanitizer
from .Logger import Logger

_pMariaDbConnection = None

_creationCommands = {
    "processvars": "CREATE TABLE IF NOT EXISTS processvars (varname VARCHAR(255), typ VARCHAR(255), value VARCHAR(255), ts TIMESTAMP, CONSTRAINT PRIMARY KEY USING HASH (varname));",
    "mmranking": "CREATE TABLE IF NOT EXISTS mmranking ( `ranks_rank` INT, `ranks_score` INT, `ranks_division_position` INT, `ranks_division_rule` VARCHAR(12) CHARACTER SET utf8, `ranks_division_minpoints` INT, `ranks_division_maxpoints` INT, `ranks_displayname` VARCHAR(50) CHARACTER SET utf8, `ranks_accountid` VARCHAR(36) CHARACTER SET utf8, `ranks_zone_name` VARCHAR(28) CHARACTER SET utf8, `ranks_zone_flag` VARCHAR(28) CHARACTER SET utf8, `ranks_zone_parent_name` VARCHAR(23) CHARACTER SET utf8, `ranks_zone_parent_flag` VARCHAR(23) CHARACTER SET utf8, `ranks_zone_parent_parent_name` VARCHAR(13) CHARACTER SET utf8, `ranks_zone_parent_parent_flag` VARCHAR(8) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_name` VARCHAR(6) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_flag` VARCHAR(6) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_parent_name` VARCHAR(5) CHARACTER SET utf8, `ranks_zone_parent_parent_parent_parent_flag` VARCHAR(3) CHARACTER SET utf8, `page` INT, `note` INT, `ts` TIMESTAMP, CONSTRAINT accountid PRIMARY KEY USING BTREE (ranks_accountid));",
    "modules" : "CREATE TABLE IF NOT EXISTS modules (channel VARCHAR(255), ts TIMESTAMP, luckerscounter INT NOT NULL DEFAULT 0, joke INT NOT NULL DEFAULT 0, kem INT NOT NULL DEFAULT 0, mm INT NOT NULL DEFAULT 0, roll INT NOT NULL DEFAULT 0, score INT NOT NULL DEFAULT 0, ooga INT NOT NULL DEFAULT 0, ping INT NOT NULL DEFAULT 0, test INT NOT NULL DEFAULT 0, CONSTRAINT PRIMARY KEY USING HASH (channel));"
}

class MariaDbWrapper(minidi.Injectable):
	pEnvironment: Environment
	pInputSanitizer: InputSanitizer
	pLogger: Logger

	def _query(self, query: str):
		try:
			cursor = _pMariaDbConnection.cursor()
			cursor.execute(query)
		except (mariadb.Error, mariadb.InterfaceError) as e:
			self.pLogger.info(f"Error connecting to MariaDB: {e}")
			self.connect()
			cursor = _pMariaDbConnection.cursor()
			cursor.execute(query)
		
		return cursor
	# def _query(self, query: str)

	def connect(self):
		global _pMariaDbConnection # use the global _pMariaDbConnection, so it doesn't create a local variable

		_pMariaDbConnection = mariadb.connect(
			user     =     self.pEnvironment.getVariable('DBUSER') ,
			password =     self.pEnvironment.getVariable('DBPASS') ,
			host     =     self.pEnvironment.getVariable('DBHOST') ,
			port     = int(self.pEnvironment.getVariable('DBPORT')),
			database =     self.pEnvironment.getVariable('DBNAME')
		)
		_pMariaDbConnection.autocommit = True
		_pMariaDbConnection.auto_reconnect = True

		self.pLogger.debug(_pMariaDbConnection.auto_reconnect)
	# def connect(self)

	def fetch(self, query: str) -> list:
		outputRows = []

		queryResult = self._query(query)
		columns = [desc[0] for desc in queryResult.description]
		rows = queryResult.fetchall()

		for row in rows:
			outputRow = {}
			for index, column in enumerate(columns):
				outputRow[column] = row[index]
			
			outputRows.append(outputRow)
		# for row in rows

		return outputRows
	# def fetch(self, query: str) -> list

	def init(self) -> bool:
		for tableName in _creationCommands.keys():
			success = self.initTable(tableName)
			if not success:
				return False
		# for tableName in _creationCommands.keys()
		
		return True
	# def init(self) -> bool

	def initTable(self, tableName: str) -> bool:
		cur = self.fetch(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{tableName}' LIMIT 1;")
		for r in cur:
			if r['COUNT(*)'] == 0:
				self.pLogger.info(f"Table '{tableName}' does not exist - creating ...")
				self.query(_creationCommands[tableName])
				self.pLogger.info(f"Successfully created table '{tableName}'!")
			# if r['COUNT(*)'] == 0

			return True
		# for r in cur

		return False
	# def initTable(self, tableName: str) -> bool

	def query(self, query: str) -> int:
		return self._query(query).rowcount
# class MariaDbWrapper(minidi.Injectable)