# vendor
import minidi

# local
from .Logger import Logger

_pDbConnection = None

class DbConnection(minidi.Injectable):
	pLogger: Logger

	def query(self, query: str):
		try:
			cursor = _pDbConnection.cursor()
			cursor.execute(query)
		except Exception as pException:
			self.pLogger.info(f"Error executing query: {pException}")
		
		return cursor
	# def query(self, query: str)

	def set(self, pDbConnection):
		global _pDbConnection
		_pDbConnection = pDbConnection
	# def set(self, pDbConnection)
# class DbConnection(minidi.Injectable)