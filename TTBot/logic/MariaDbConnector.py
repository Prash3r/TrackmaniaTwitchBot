# vendor
import minidi

# local
from .MariaDbConnection import MariaDbConnection

class MariaDbConnector(minidi.Injectable):
	pMariaDbConnection: MariaDbConnection

	def fetch(self, query: str) -> list:
		outputRows = []

		pQueryResult = self.pMariaDbConnection.query(query)
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
		return self.pMariaDbConnection.query(query).rowcount
# class MariaDbConnector(minidi.Injectable)