# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.logic.Logger import Logger
from TTBot.logic.DbConnector import DbConnector

class TestLocalVariables(unittest.TestCase):
	def test_get_default(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.info = mock.Mock()

		rows = []

		pDbConnector = DbConnector()
		pDbConnector.execute = mock.Mock()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pLocalVariables = LocalVariables()
		pLocalVariables.pInputSanitizer = pInputSanitizer
		pLocalVariables.pLogger = pLogger
		pLocalVariables.pDbConnector = pDbConnector

		localVariable = pLocalVariables.get('local%variable', 'channel%', 0)
		self.assertEqual(localVariable, 0)

		pLogger.info.assert_called_once_with("Retrieving local variable 'localvariable' for channel 'channel' failed - no data in DB!")
		pDbConnector.execute.assert_called_once()
		pDbConnector.fetch.assert_called_once()
	# def test_get_default(self)

	def test_get_normal(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()

		rows = [{'typ': 'int', 'value': '42'}]

		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pLocalVariables = LocalVariables()
		pLocalVariables.pInputSanitizer = pInputSanitizer
		pLocalVariables.pLogger = pLogger
		pLocalVariables.pDbConnector = pDbConnector

		localVariable = pLocalVariables.get('local%variable', 'channel%', 0)
		self.assertEqual(localVariable, 42)

		pDbConnector.fetch.assert_called_once()
	# def test_get_normal(self)

	def test_get_queryError(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.error = mock.Mock()

		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(side_effect=Exception(''))

		pLocalVariables = LocalVariables()
		pLocalVariables.pInputSanitizer = pInputSanitizer
		pLocalVariables.pLogger = pLogger
		pLocalVariables.pDbConnector = pDbConnector

		localVariable = pLocalVariables.get('local%variable', 'channel%', 0)
		self.assertEqual(localVariable, 0)

		pLogger.error.assert_called_once_with("Retrieving local variable 'localvariable' for channel 'channel' failed - error in query!")
		pDbConnector.fetch.assert_called_once()
	# def test_get_queryError(self)

	def test_get_typeMismatch(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.error = mock.Mock()

		rows = [{'typ': 'int', 'value': '42'}]

		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pLocalVariables = LocalVariables()
		pLocalVariables.pInputSanitizer = pInputSanitizer
		pLocalVariables.pLogger = pLogger
		pLocalVariables.pDbConnector = pDbConnector

		localVariable = pLocalVariables.get('local%variable', 'channel%', '0')
		self.assertEqual(localVariable, '0')

		pLogger.error.assert_called_once_with("Mismatched type of local variable 'localvariable' for channel 'channel': 'int' (database) != 'str' (default)")
		pDbConnector.fetch.assert_called_once()
	# def test_get_typeMismatch(self)

	def test_write_False(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		pDbConnector = DbConnector()
		pDbConnector.execute = mock.Mock(side_effect=ConnectionError())

		pLocalVariables = LocalVariables()
		pLocalVariables.pInputSanitizer = pInputSanitizer
		pLocalVariables.pLogger = pLogger
		pLocalVariables.pDbConnector = pDbConnector

		self.assertFalse(pLocalVariables.write('local%variable', 'channel%', 'Hello, World!'))

		pLogger.debug.assert_not_called()
		pLogger.error.assert_called_once_with("FAILED to update local variable 'localvariable' for channel 'channel' to 'Hello, World!'!")
		pDbConnector.execute.assert_called_once()
	# def test_write_False(self)

	def test_write_True(self):
		pInputSanitizer = InputSanitizer()

		pLogger = Logger()
		pLogger.debug = mock.Mock()
		pLogger.error = mock.Mock()

		pDbConnector = DbConnector()
		pDbConnector.execute = mock.Mock()

		pLocalVariables = LocalVariables()
		pLocalVariables.pInputSanitizer = pInputSanitizer
		pLocalVariables.pLogger = pLogger
		pLocalVariables.pDbConnector = pDbConnector

		self.assertTrue(pLocalVariables.write('local%variable', 'channel%', 'Hello, World!'))

		pLogger.debug.assert_called_once_with("Updated local variable 'localvariable' for channel 'channel' to 'Hello, World!'!")
		pLogger.error.assert_not_called()
		pDbConnector.execute.assert_called_once()
	# def test_write_True(self)
# class TestLocalVariables(unittest.TestCase)