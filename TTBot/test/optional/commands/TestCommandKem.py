# pylib
import asyncio
import unittest
from unittest import mock

# local
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.optional.commands.CommandKem import CommandKem

class TestCommandKem(unittest.TestCase):
	def test_getCommandString(self):
		pCommandKem = CommandKem()
		self.assertEqual(pCommandKem.getCommandString(), 'kem')
	# def test_getCommandString(self)

	def test_getRightsId(self):
		pCommandKem = CommandKem()
		self.assertEqual(pCommandKem.getRightsId(), 'kem')
	# def test_getRightsId(self)

	def runTestExecute(self, pCommandKem: CommandKem, args: list, result: str):
		loop = asyncio.get_event_loop()
		pCoroutine = pCommandKem.execute(object(), args)
		coroutineResult = loop.run_until_complete(asyncio.gather(pCoroutine))
		self.assertEqual(coroutineResult[0], result)
	# def runTestExecute(self, pCommandKem: CommandKem, args: list, result: str)

	def test_execute_default(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		self.runTestExecute(pCommandKem, [], "kem1W")

		pInputSanitizer.isInteger.assert_not_called()
	# def test_execute_default(self)

	def test_execute_argumentInteger5(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		self.runTestExecute(pCommandKem, [5, 'unused'], "kem1W kem1W kem1W kem1W kem1W")

		pInputSanitizer.isInteger.assert_called_once_with(5)
	# def test_execute_argumentInteger5(self)

	def test_execute_argumentStringMinus5(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		self.runTestExecute(pCommandKem, ['-5', 'unused'], "kem1W")

		pInputSanitizer.isInteger.assert_called_once_with('-5')
	# def test_execute_argumentStringMinus5(self)

	def test_execute_argumentString5(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		self.runTestExecute(pCommandKem, ['5', 'unused'], "kem1W kem1W kem1W kem1W kem1W")

		pInputSanitizer.isInteger.assert_called_once_with('5')
	# def test_execute_argumentString5(self)

	def test_execute_argumentString15(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		self.runTestExecute(pCommandKem, ['15', 'unused'], "kem1W kem1W kem1W kem1W kem1W kem1W kem1W kem1W kem1W kem1W")

		pInputSanitizer.isInteger.assert_called_once_with('15')
	# def test_execute_argumentString15(self)
# class TestCommandKem(unittest.TestCase)