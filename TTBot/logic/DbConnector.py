# vendor
import minidi

# local
from TTBot.logic.DbConnection import DbConnection

class DbConnector(minidi.Injectable):
	pDbConnection: DbConnection

	def execute(self, query: str, inputs: list = []) -> int:
		pQueryResult = self.pDbConnection.query(query, inputs)
		return pQueryResult.rowcount
	# def execute(self, query: str) -> int

	def fetch(self, query: str, inputs: list = []) -> list:
		outputRows = []

		pQueryResult = self.pDbConnection.query(query, inputs)
		columns = [desc[0] for desc in pQueryResult.description]
		rows = pQueryResult.fetchall()

		for row in rows:
			outputRow = {}
			for index, column in enumerate(columns):
				outputRow[column] = row[index]
			
			outputRows.append(outputRow)
		# for row in rows

		return outputRows
	# def fetch(self, query: str) -> list

	def getColumns(self, table: str) -> list:
		# cannot use ? placeholder, but this is in control of the code -> no security risk
		query = f"SELECT * FROM `{table}` WHERE 0=1;"
		pQueryResult = self.pDbConnection.query(query)
		return [desc[0] for desc in pQueryResult.description]
	# def getColumns(self, table: str) -> list
# class DbConnector(minidi.Injectable)