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

# if you need remanent data in the database put your process vars here:
_processVariables = {
    "luckerscounter": {
        "typ": "int",
        "defaultvalue": 0
    },
    "hoursonline": {
        "typ": "int",
        "defaultvalue": 0
    },
    "lastjoker": {
        "typ": "str",
        "defaultvalue": "Fegir"
    },
    "shamename": {
        "typ": "str",
        "defaultvalue": "prash3r"
    },
    "shamecounter": {
        "typ": "int",
        "defaultvalue": 3
    },
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
		return self._query(query).fetchall()
	# def fetch(self, query: str) -> list

	def getProcessVariable(self, processVariableName: str):
		processVariableName = self.pInputSanitizer.sanitize(processVariableName)
		processVariableName = processVariableName.replace(' ', '')

		try:
			cur = self.fetch(f"SELECT varname, typ, value FROM processvars WHERE varname = '{processVariableName}' LIMIT 1;")
			# should be either a hit or we must ingest the default value
			for (_, _, value) in cur:
				if _processVariables[processVariableName]['typ'] == 'int':
					return int(value)
				if _processVariables[processVariableName]['typ'] == 'float':
					return float(value)
				else: # String
					return value
			self.pLogger.error(f"Retrieving process variable '{processVariableName}' failed - no data in DB!")
			return _processVariables[processVariableName]['defaultvalue'] # return defaultvalue when cur doesnt carry data
		except:
			self.pLogger.error(f"Retrieving process variable '{processVariableName}' failed - error in query!")
			return _processVariables[processVariableName]['defaultvalue'] # return defaultvalue when db command fails
	# def getProcessVariable(self, processVariableName: str)

	def init(self) -> bool:
		success = True
		for table in _creationCommands.keys():
			success = success and self.initTable(table)
		
		success = success and self.initProcessVariables()
		return success
	# def init(self) -> bool

	def initTable(self, tablename) -> bool:
		cur = self.fetch(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{tablename}' LIMIT 1;")
		for r in cur:
			if r[0] == 0:
				self.pLogger.info(f"Table '{tablename}' does not exist - creating ...")
				self.query(_creationCommands[tablename])
				self.pLogger.info(f"Successfully created table '{tablename}'!")
			# if r[0] == 0

			return True
		# for r in cur

		return False
	# def initTable(self, tablename) -> bool

	def initProcessVariables(self) -> bool:
		try:
			for key, processVariable in _processVariables.items():
				self.query(f"INSERT IGNORE INTO processvars SET varname = '{key}', typ = '{processVariable['typ']}', value = '{processVariable['defaultvalue']}';")

			return True
		except:
			self.pLogger.error(f"Could not initialize process variable '{key}'!")
			return False
	# def initProcessVariables(self) -> bool

	def query(self, query: str) -> int:
		return self._query(query).rowcount
	# def query(self, query: str) -> int

	def writeProcessVariable(self, processVariableName: str, newvalue, oldvalue='unknown'):
		processVariableName = self.pInputSanitizer.sanitize(processVariableName)
		processVariableName = processVariableName.replace(' ', '')
		
		try:
			self.query(f"UPDATE processvars SET value = '{newvalue}' WHERE varname = '{processVariableName}' LIMIT 1;")
			self.pLogger.debug(f"Updated process variable '{processVariableName}' from '{oldvalue}' to '{newvalue}'!")
		except:
			self.pLogger.error(f"FAILED to update process variable '{processVariableName}' from '{oldvalue}' to '{newvalue}'!")
	# def writeProcessVariable(self, processVariableName: str, newvalue, oldvalue='unknown')
# class MariaDbWrapper(minidi.Injectable)