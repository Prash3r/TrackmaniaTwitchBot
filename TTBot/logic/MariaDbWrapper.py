# vendor
import mariadb
import minidi

# local
from .Environment import Environment
from .InputSanitizer import InputSanitizer
from .Logger import Logger

_pMariaDbConnection = None

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

	def query(self, query: str) -> int:
		return self._query(query).rowcount
# class MariaDbWrapper(minidi.Injectable)