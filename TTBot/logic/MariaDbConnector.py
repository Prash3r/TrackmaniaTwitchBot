# vendor
import minidi

# local
from .DbConnection import DbConnection

class MariaDbConnector(minidi.Injectable):
	pDbConnection: DbConnection

	def fetch(self, query: str) -> list:
		outputRows = []

		pQueryResult = self.pDbConnection.query(query)
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

	def query(self, query: str) -> int:
		return self.pDbConnection.query(query).rowcount
# class MariaDbConnector(minidi.Injectable)