# vendor
import minidi

# local
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter
from TTBot.logic.Logger import Logger

_pDbConnection = None

class DbConnection(minidi.Injectable):
	pLogger: Logger
	pDbQueryDialectConverter: DbQueryDialectConverter

	def query(self, query: str):
		query = self.pDbQueryDialectConverter.convert(query)

		try:
			cursor = _pDbConnection.cursor()
			cursor.execute(query)
		except Exception as pException:
			self.pLogger.info(f"Error executing query: {pException}")
			self.pLogger.debug(query)
		
		return cursor
	# def query(self, query: str)

	def set(self, pDbConnection):
		global _pDbConnection
		_pDbConnection = pDbConnection
	# def set(self, pDbConnection)
# class DbConnection(minidi.Injectable)