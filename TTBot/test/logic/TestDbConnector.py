# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.DbConnector import DbConnector

class QueryResult:
	description = ''
	rowcount = 0

	def fetchall(self):
		pass
# class QueryResult

class TestDbConnector(unittest.TestCase):
	def test_execute(self):
		pQueryResult = QueryResult()
		pQueryResult.rowcount = 1

		pDbConnection = DbConnection()
		pDbConnection.query = mock.Mock(return_value=pQueryResult)

		pDbConnector = DbConnector()
		pDbConnector.pDbConnection = pDbConnection

		rowcount = pDbConnector.execute("UPDATE `modules` SET `ping` = 1 WHERE `channel` = 'unittest'")
		self.assertEqual(rowcount, 1)

		pDbConnection.query.assert_called_once_with("UPDATE `modules` SET `ping` = 1 WHERE `channel` = 'unittest'", [])
	# def test_execute(self)

	def test_fetch(self):
		pQueryResult = QueryResult()
		pQueryResult.description = [['rank', 'INT(11)'], ['player', 'VARCHAR(32)']]
		pQueryResult.fetchall = mock.Mock(return_value=[[1, 'Forever'], [2, 'Wirtual'], [3, 'Scrapie']])

		pDbConnection = DbConnection()
		pDbConnection.query = mock.Mock(return_value=pQueryResult)

		pDbConnector = DbConnector()
		pDbConnector.pDbConnection = pDbConnection

		rows = pDbConnector.fetch("SELECT `rank`, `player` FROM `ranking` WHERE `rank` <= 3;")
		self.assertEqual(len(rows), 3)
		self.assertDictEqual({'rank': 1, 'player': 'Forever'}, rows[0])
		self.assertDictEqual({'rank': 2, 'player': 'Wirtual'}, rows[1])
		self.assertDictEqual({'rank': 3, 'player': 'Scrapie'}, rows[2])

		pQueryResult.fetchall.assert_called_once()
		pDbConnection.query.assert_called_once_with("SELECT `rank`, `player` FROM `ranking` WHERE `rank` <= 3;", [])
	# def test_fetch(self)

	def test_getColumns(self):
		pQueryResult = QueryResult()
		pQueryResult.description = [['rank', 'INT(11)'], ['player', 'VARCHAR(32)']]
		pQueryResult.fetchall = mock.Mock()

		pDbConnection = DbConnection()
		pDbConnection.query = mock.Mock(return_value=pQueryResult)

		pDbConnector = DbConnector()
		pDbConnector.pDbConnection = pDbConnection

		columns = pDbConnector.getColumns('ranking')
		self.assertListEqual(columns, ['rank', 'player'])

		pQueryResult.fetchall.assert_not_called()
		pDbConnection.query.assert_called_once_with("SELECT * FROM `ranking` WHERE 0=1;")
	# def test_getColumns(self)
# class TestDbConnector(unittest.TestCase)