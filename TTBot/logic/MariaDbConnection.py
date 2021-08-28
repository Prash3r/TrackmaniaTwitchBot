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

	def query(self, query: str):
		try:
			cursor = _pMariaDbConnection.cursor()
			cursor.execute(query)
		except (mariadb.Error, mariadb.InterfaceError) as e:
			self.pLogger.info(f"Error executing query: {e}")
		
		return cursor
	# def query(self, query: str)

	def set(self, pMariaDbConnection):
		global _pMariaDbConnection
		_pMariaDbConnection = pMariaDbConnection
	# def set(self, pMariaDbConnection)
# class MariaDbConnection(minidi.Injectable)