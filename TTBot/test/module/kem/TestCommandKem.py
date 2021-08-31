# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.module.kem.CommandKem import CommandKem

class TestCommandKem(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandString(self):
		pCommandKem = CommandKem()
		self.assertEqual(pCommandKem.getCommandString(), 'kem')
	# async def test_getCommandString(self)

	async def test_getModuleId(self):
		pCommandKem = CommandKem()
		self.assertEqual(pCommandKem.getModuleId(), 'kem')
	# async def test_getModuleId(self)

	async def test_execute_default(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		result = await pCommandKem.execute(object(), [])
		self.assertEqual(result, "kem1W")

		pInputSanitizer.isInteger.assert_not_called()
	# async def test_execute_default(self)

	async def test_execute_argumentInteger5(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		result = await pCommandKem.execute(object(), [5, 'unused'])
		self.assertEqual(result, "kem1W kem1W kem1W kem1W kem1W")

		pInputSanitizer.isInteger.assert_called_once_with(5)
	# async def test_execute_argumentInteger5(self)

	async def test_execute_argumentStringMinus5(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		result = await pCommandKem.execute(object(), ['-5', 'unused'])
		self.assertEqual(result, "kem1W")

		pInputSanitizer.isInteger.assert_called_once_with('-5')
	# async def test_execute_argumentStringMinus5(self)

	async def test_execute_argumentString5(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		result = await pCommandKem.execute(object(), ['5', 'unused'])
		self.assertEqual(result, "kem1W kem1W kem1W kem1W kem1W")

		pInputSanitizer.isInteger.assert_called_once_with('5')
	# async def test_execute_argumentString5(self)

	async def test_execute_argumentString15(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pCommandKem = CommandKem()
		pCommandKem.pInputSanitizer = pInputSanitizer

		result = await pCommandKem.execute(object(), ['15', 'unused'])
		self.assertEqual(result, "kem1W kem1W kem1W kem1W kem1W kem1W kem1W kem1W kem1W kem1W")

		pInputSanitizer.isInteger.assert_called_once_with('15')
	# async def test_execute_argumentString15(self)
# class TestCommandKem(unittest.IsolatedAsyncioTestCase)