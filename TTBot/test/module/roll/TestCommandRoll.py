# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Randomizer import Randomizer
from TTBot.module.roll.CommandRoll import CommandRoll

class TestCommandRoll(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandTrigger(self):
		pCommandRoll = CommandRoll()
		self.assertEqual(pCommandRoll.getCommandTrigger(), 'roll')
	# async def test_getCommandTrigger(self)

	async def test_getModuleId(self):
		pCommandRoll = CommandRoll()
		self.assertEqual(pCommandRoll.getModuleId(), 'roll')
	# async def test_getModuleId(self)

	async def test_execute_default(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=1337)

		pCommandRoll = CommandRoll()
		pCommandRoll.pInputSanitizer = pInputSanitizer
		pCommandRoll.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pCommandRoll.execute(pMessage, [])
		self.assertEqual(result, "@unittest Use '!roll <max>' to roll a number out of max!")

		pInputSanitizer.isInteger.assert_not_called()
		pRandomizer.uniformInt.assert_not_called()
	# async def test_execute_default(self)

	async def test_execute_default6(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=4)

		pCommandRoll = CommandRoll()
		pCommandRoll.pInputSanitizer = pInputSanitizer
		pCommandRoll.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pCommandRoll.execute(pMessage, ['6', 'unused'])
		self.assertEqual(result, "@unittest 4/6")

		pInputSanitizer.isInteger.assert_called_once_with('6')
		pRandomizer.uniformInt.assert_called_once_with(1, 6)
	# async def test_execute_default6(self)

	async def test_execute_special69(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=69)

		pCommandRoll = CommandRoll()
		pCommandRoll.pInputSanitizer = pInputSanitizer
		pCommandRoll.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pCommandRoll.execute(pMessage, ['100', 'unused'])
		self.assertEqual(result, "@unittest 69/100 - NICE")

		pInputSanitizer.isInteger.assert_called_once_with('100')
		pRandomizer.uniformInt.assert_called_once_with(1, 100)
	# async def test_execute_special69(self)

	async def test_execute_special420(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=169)

		pCommandRoll = CommandRoll()
		pCommandRoll.pInputSanitizer = pInputSanitizer
		pCommandRoll.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pCommandRoll.execute(pMessage, ['420', 'unused'])
		self.assertEqual(result, "@unittest we do not support drugs in this chat (169/420)")

		pInputSanitizer.isInteger.assert_called_once_with('420')
		pRandomizer.uniformInt.assert_called_once_with(1, 420)
	# async def test_execute_special420(self)
# class TestCommandRoll(unittest.IsolatedAsyncioTestCase)