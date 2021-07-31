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

		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(return_value=rows)
		pMariaDbWrapper.query = mock.Mock()

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbWrapper = pMariaDbWrapper

		processVariable = pProcessVariables.get('process%variable', 0)
		self.assertEqual(processVariable, 0)
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pLogger.info.assert_called_once_with("Retrieving process variable 'processvariable' failed - no data in DB!")
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
		pMariaDbWrapper.query.assert_called_once_with("INSERT IGNORE INTO processvars SET varname = 'processvariable', typ = 'int', value = '0';")
	# def test_get_default(self)

	def test_get_normal(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()

		rows = [['int', '42']]

		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(return_value=rows)

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbWrapper = pMariaDbWrapper

		processVariable = pProcessVariables.get('process%variable', 0)
		self.assertEqual(processVariable, 42)
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
	# def test_get_normal(self)

	def test_get_queryError(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()
		pLogger.error = mock.Mock()

		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(side_effect=Exception(''))

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbWrapper = pMariaDbWrapper

		processVariable = pProcessVariables.get('process%variable', 0)
		self.assertEqual(processVariable, 0)
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pLogger.error.assert_called_once_with("Retrieving process variable 'processvariable' failed - error in query!")
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
	# def test_get_queryError(self)

	def test_get_typeMismatch(self):
		pInputSanitizer = mock.Mock()
		pInputSanitizer.sanitize = mock.Mock(return_value='process variable')

		pLogger = mock.Mock()
		pLogger.error = mock.Mock()

		rows = [['int', '42']]

		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(return_value=rows)

		pProcessVariables = ProcessVariables()
		pProcessVariables.pInputSanitizer = pInputSanitizer
		pProcessVariables.pLogger = pLogger
		pProcessVariables.pMariaDbWrapper = pMariaDbWrapper

		processVariable = pProcessVariables.get('process%variable', '0')
		self.assertEqual(processVariable, '0')
		pInputSanitizer.sanitize.assert_called_once_with('process%variable')
		pLogger.error.assert_called_once_with("Mismatched type of process variable 'processvariable': 'int' (database) != 'str' (default)!")
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT typ, value FROM processvars WHERE varname = 'processvariable' LIMIT 1;")
	# def test_get_typeMismatch(self)
# class TestProcessVariables(unittest.TestCase)