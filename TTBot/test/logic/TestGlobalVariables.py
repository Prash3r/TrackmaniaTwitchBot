# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger

class TestGlobalVariables(unittest.TestCase):
	def test_get_default(self):
		rows = []

		pDbConnector = DbConnector()
		pDbConnector.execute = mock.Mock()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.info = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pDbConnector = pDbConnector

		globalVariable = pGlobalVariables.get('global%variable', 0)
		self.assertEqual(globalVariable, 0)

		pLogger.info.assert_called_once_with("Retrieving global variable 'globalvariable' failed - no data in DB!")
		pDbConnector.execute.assert_called_once()
		pDbConnector.fetch.assert_called_once()
	# def test_get_default(self)

	def test_get_normal(self):
		rows = [{'typ': 'int', 'value': '42'}]

		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pInputSanitizer = InputSanitizer()

		pLogger = Logger()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pDbConnector = pDbConnector

		globalVariable = pGlobalVariables.get('global%variable', 0)
		self.assertEqual(globalVariable, 42)

		pDbConnector.fetch.assert_called_once()
	# def test_get_normal(self)

	def test_get_queryError(self):
		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(side_effect=Exception(''))

		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.error = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pDbConnector = pDbConnector

		globalVariable = pGlobalVariables.get('global%variable', 0)
		self.assertEqual(globalVariable, 0)

		pLogger.error.assert_called_once_with("Retrieving global variable 'globalvariable' failed - error in query!")
		pDbConnector.fetch.assert_called_once()
	# def test_get_queryError(self)

	def test_get_typeMismatch(self):
		rows = [{'typ': 'int', 'value': '42'}]

		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.error = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pDbConnector = pDbConnector

		globalVariable = pGlobalVariables.get('global%variable', '0')
		self.assertEqual(globalVariable, '0')

		pLogger.error.assert_called_once_with("Mismatched type of global variable 'globalvariable': 'int' (database) != 'str' (default)")
		pDbConnector.fetch.assert_called_once()
	# def test_get_typeMismatch(self)

	def test_write_False(self):
		pDbConnector = DbConnector()
		pDbConnector.execute = mock.Mock(side_effect=ConnectionError())

		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pDbConnector = pDbConnector

		self.assertFalse(pGlobalVariables.write('global%variable', 'Hello, World!'))

		pLogger.debug.assert_not_called()
		pLogger.error.assert_called()
		pDbConnector.execute.assert_called()
	# def test_write_False(self)

	def test_write_True(self):
		pDbConnector = DbConnector()
		pDbConnector.execute = mock.Mock()

		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pDbConnector = pDbConnector

		self.assertTrue(pGlobalVariables.write('global%variable', 'Hello, World!'))

		pLogger.debug.assert_called_once_with("Updated global variable 'globalvariable' to 'Hello, World!'!")
		pLogger.error.assert_not_called()
		pDbConnector.execute.assert_called_once()
	# def test_write_True(self)
# class TestGlobalVariables(unittest.TestCase)