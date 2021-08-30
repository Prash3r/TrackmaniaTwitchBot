# pylib
import re

# local
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter

class SqliteQueryDialectConverter(DbQueryDialectConverter):
	def convert(self, query: str) -> str:
		query = re.sub(r'USING (HASH|BTREE)', '', query, flags=re.IGNORECASE)
		query = re.sub(r'CHARACTER SET \w', '', query, flags=re.IGNORECASE)
		return query
	# def convert(self, query: str) -> str
# class SqliteQueryDialectConverter(DbQueryDialectConverter)