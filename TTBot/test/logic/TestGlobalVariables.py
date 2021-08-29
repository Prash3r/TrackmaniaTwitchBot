# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger
from TTBot.logic.MariaDbConnector import MariaDbConnector

class TestGlobalVariables(unittest.TestCase):
	def test_get_default(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.info = mock.Mock()

		rows = []

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)
		pMariaDbConnector.query = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pMariaDbConnector = pMariaDbConnector

		globalVariable = pGlobalVariables.get('global%variable', 0)
		self.assertEqual(globalVariable, 0)

		pLogger.info.assert_called_once_with("Retrieving global variable 'globalvariable' failed - no data in DB!")
		pMariaDbConnector.fetch.assert_called_once()
		pMariaDbConnector.query.assert_called_once()
	# def test_get_default(self)

	def test_get_normal(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()

		rows = [{'typ': 'int', 'value': '42'}]

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pMariaDbConnector = pMariaDbConnector

		globalVariable = pGlobalVariables.get('global%variable', 0)
		self.assertEqual(globalVariable, 42)

		pMariaDbConnector.fetch.assert_called_once()
	# def test_get_normal(self)

	def test_get_queryError(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.error = mock.Mock()

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.fetch = mock.Mock(side_effect=Exception(''))

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pMariaDbConnector = pMariaDbConnector

		globalVariable = pGlobalVariables.get('global%variable', 0)
		self.assertEqual(globalVariable, 0)

		pLogger.error.assert_called_once_with("Retrieving global variable 'globalvariable' failed - error in query!")
		pMariaDbConnector.fetch.assert_called_once()
	# def test_get_queryError(self)

	def test_get_typeMismatch(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.error = mock.Mock()

		rows = [{'typ': 'int', 'value': '42'}]

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pMariaDbConnector = pMariaDbConnector

		globalVariable = pGlobalVariables.get('global%variable', '0')
		self.assertEqual(globalVariable, '0')

		pLogger.error.assert_called_once_with("Mismatched type of global variable 'globalvariable': 'int' (database) != 'str' (default)")
		pMariaDbConnector.fetch.assert_called_once()
	# def test_get_typeMismatch(self)

	def test_write_False(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.query = mock.Mock(side_effect=ConnectionError())

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pMariaDbConnector = pMariaDbConnector

		self.assertFalse(pGlobalVariables.write('global%variable', 'Hello, World!'))

		pLogger.debug.assert_not_called()
		pLogger.error.assert_called_once_with("FAILED to update global variable 'globalvariable' to 'Hello, World!'!")
		pMariaDbConnector.query.assert_called_once()
	# def test_write_False(self)

	def test_write_True(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.query = mock.Mock()

		pGlobalVariables = GlobalVariables()
		pGlobalVariables.pInputSanitizer = pInputSanitizer
		pGlobalVariables.pLogger = pLogger
		pGlobalVariables.pMariaDbConnector = pMariaDbConnector

		self.assertTrue(pGlobalVariables.write('global%variable', 'Hello, World!'))

		pLogger.debug.assert_called_once_with("Updated global variable 'globalvariable' to 'Hello, World!'!")
		pLogger.error.assert_not_called()
		pMariaDbConnector.query.assert_called_once()
	# def test_write_True(self)
# class TestGlobalVariables(unittest.TestCase)