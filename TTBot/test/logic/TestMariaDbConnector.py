# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.MariaDbConnector import MariaDbConnector

class QueryResult:
	description = ''
	rowcount = 0

	def fetchall(self):
		pass
# class QueryResult

class TestMariaDbConnector(unittest.TestCase):
	def test_fetch(self):
		pQueryResult = QueryResult()
		pQueryResult.description = [['rank', 'INT(11)'], ['player', 'VARCHAR(32)']]
		pQueryResult.fetchall = mock.Mock(return_value=[[1, 'Forever'], [2, 'Wirtual'], [3, 'Scrapie']])

		pDbConnection = DbConnection()
		pDbConnection.query = mock.Mock(return_value=pQueryResult)

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.pDbConnection = pDbConnection

		rows = pMariaDbConnector.fetch("SELECT `rank`, `player` FROM `ranking` WHERE `rank` <= 3;")
		self.assertEqual(len(rows), 3)
		self.assertDictEqual({'rank': 1, 'player': 'Forever'}, rows[0])
		self.assertDictEqual({'rank': 2, 'player': 'Wirtual'}, rows[1])
		self.assertDictEqual({'rank': 3, 'player': 'Scrapie'}, rows[2])

		pQueryResult.fetchall.assert_called_once()
		pDbConnection.query.assert_called_once_with("SELECT `rank`, `player` FROM `ranking` WHERE `rank` <= 3;")
	# def test_fetch(self)

	def test_query(self):
		pQueryResult = QueryResult()
		pQueryResult.rowcount = 1

		pDbConnection = DbConnection()
		pDbConnection.query = mock.Mock(return_value=pQueryResult)

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.pDbConnection = pDbConnection

		rowcount = pMariaDbConnector.query("UPDATE `modules` SET `ping` = 1 WHERE `channel` = 'unittest'")
		self.assertEqual(rowcount, 1)

		pDbConnection.query.assert_called_once_with("UPDATE `modules` SET `ping` = 1 WHERE `channel` = 'unittest'")
	# def test_query(self)
# class TestMariaDbConnector(unittest.TestCase)