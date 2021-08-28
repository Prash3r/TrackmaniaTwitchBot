# vendor
import mariadb
import minidi

# local
from .Environment import Environment
from .Logger import Logger

_pMariaDbConnection = None

class MariaDbConnection(minidi.Injectable):
	pEnvironment: Environment
	pLogger: Logger

	def connect(self):
		# use the global _pMariaDbConnection, so it doesn't create a local variable
		global _pMariaDbConnection

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

	def query(self, query: str):
		try:
			cursor = _pMariaDbConnection.cursor()
			cursor.execute(query)
		except (mariadb.Error, mariadb.InterfaceError) as e:
			self.pLogger.info(f"Error connecting to MariaDB: {e}")
			self.connect()
			cursor = _pMariaDbConnection.cursor()
			cursor.execute(query)
		
		return cursor
	# def query(self, query: str)
# class MariaDbConnection(minidi.Injectable)