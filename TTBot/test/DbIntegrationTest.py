# pylib
import os
import sqlite3
import unittest
from unittest import mock

# vendor
import minidi

# local
from TTBot.logic.development.SqliteQueryDialectConverter import SqliteQueryDialectConverter
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.Logger import Logger

class DbIntegrationTest(unittest.TestCase):
	def setUpBeforeEach(self, dbName: str):
		pLogger: Logger = minidi.get(Logger)
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		minidi.set(DbQueryDialectConverter, minidi.get(SqliteQueryDialectConverter))

		pSqliteDbConnection = sqlite3.connect(dbName, isolation_level=None)
		pDbConnection: DbConnection = minidi.get(DbConnection)
		pDbConnection.set(pSqliteDbConnection)

		pDbConnection.query("PRAGMA encoding = 'UTF-8';")
	# def setUpBeforeEach(self, dbName: str)

	def tearDownAfterEach(self, dbName: str):
		pDbConnection: DbConnection = minidi.get(DbConnection)
		pDbConnection.set(None)

		os.remove(dbName)
	# def tearDownAfterEach(self, dbName: str)
# class DbIntegrationTest(unittest.TestCase)