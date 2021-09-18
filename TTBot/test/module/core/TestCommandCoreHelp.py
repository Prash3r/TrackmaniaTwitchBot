# pylib
import unittest

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.module.core.CommandCoreHelp import CommandCoreHelp

class TestCommandCoreHelp(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandTrigger(self):
		pCommandCoreHelp = CommandCoreHelp()
		self.assertEqual(pCommandCoreHelp.getCommandTrigger(), 'help')
	# async def test_getCommandTrigger(self)

	async def test_getModuleId(self):
		pCommandCoreHelp = CommandCoreHelp()
		self.assertEqual(pCommandCoreHelp.getModuleId(), 'core')
	# async def test_getModuleId(self)

	async def test_execute(self):
		pMessage = Message(author=MessageAuthor(name='unittest'))
		pCommandCoreHelp = CommandCoreHelp()
		
		actualMessage = await pCommandCoreHelp.execute(pMessage, [])
		expectedMessage = f"@unittest {CommandCoreHelp.DEFAULT_HELP_MESSAGE}"
		self.assertEqual(actualMessage, expectedMessage)

		for specialHelpMessageKey in CommandCoreHelp.HELP_MESSAGES.keys():
			actualMessage = await pCommandCoreHelp.execute(pMessage, [specialHelpMessageKey])
			expectedMessage = f"@unittest {CommandCoreHelp.HELP_MESSAGES[specialHelpMessageKey]}"
			self.assertEqual(actualMessage, expectedMessage)
		# for specialHelpMessageKey in CommandCoreHelp.HELP_MESSAGES.keys()
		
		actualMessage = await pCommandCoreHelp.execute(pMessage, ['kem1W'])
		expectedMessage = f"@unittest {CommandCoreHelp.DEFAULT_HELP_MESSAGE}"
		self.assertEqual(actualMessage, expectedMessage)
	# async def test_execute(self)
# class TestCommandCoreHelp(unittest.IsolatedAsyncioTestCase)