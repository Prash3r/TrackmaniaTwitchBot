# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.ProcessVariables import ProcessVariables

class TestProcessVariables(unittest.TestCase):
	def test_get_default(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()
		pLogger.info = mock.Mock()

		rows = []

		pMariaDbConnector = mock.Mock()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)
		pMariaDbConnector.query = mock.Mock()

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbConnector = pMariaDbConnector

		processVariable = pProcessVariables.get('process%variable', 0)
		self.assertEqual(processVariable, 0)

		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pLogger.info.assert_called_once_with("Retrieving process variable 'processvariable' failed - no data in DB!")
		pMariaDbConnector.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
		pMariaDbConnector.query.assert_called_once_with("INSERT IGNORE INTO processvars SET varname = 'processvariable', typ = 'int', value = '0';")
	# def test_get_default(self)

	def test_get_normal(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()

		rows = [{'typ': 'int', 'value': '42'}]

		pMariaDbConnector = mock.Mock()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbConnector = pMariaDbConnector

		processVariable = pProcessVariables.get('process%variable', 0)
		self.assertEqual(processVariable, 42)
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pMariaDbConnector.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
	# def test_get_normal(self)

	def test_get_queryError(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()
		pLogger.error = mock.Mock()

		pMariaDbConnector = mock.Mock()
		pMariaDbConnector.fetch = mock.Mock(side_effect=Exception(''))

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbConnector = pMariaDbConnector

		processVariable = pProcessVariables.get('process%variable', 0)
		self.assertEqual(processVariable, 0)
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pLogger.error.assert_called_once_with("Retrieving process variable 'processvariable' failed - error in query!")
		pMariaDbConnector.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
	# def test_get_queryError(self)

	def test_get_typeMismatch(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()
		pLogger.error = mock.Mock()

		rows = [{'typ': 'int', 'value': '42'}]

		pMariaDbConnector = mock.Mock()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbConnector = pMariaDbConnector

		processVariable = pProcessVariables.get('process%variable', '0')
		self.assertEqual(processVariable, '0')
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pLogger.error.assert_called_once_with("Mismatched type of process variable 'processvariable': 'int' (database) != 'str' (default)!")
		pMariaDbConnector.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
	# def test_get_typeMismatch(self)
# class TestProcessVariables(unittest.TestCase)