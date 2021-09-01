# local
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter

class MariaDbQueryDialectConverter(DbQueryDialectConverter):
	def convert(self, query: str) -> str:
		return query
# class MariaDbQueryDialectConverter(DbQueryDialectConverter)