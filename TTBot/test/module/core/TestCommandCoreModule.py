# pylib
import unittest
from unittest import mock

# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.logic.UserLevel import UserLevel
from TTBot.module.core.CommandCoreModule import CommandCoreModule

class TestCommandCoreModule(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandTrigger(self):
		pCommandCoreModule = CommandCoreModule()
		self.assertEqual(pCommandCoreModule.getCommandTrigger(), 'module')
	# async def test_getCommandTrigger(self)

	async def test_getModuleId(self):
		pCommandCoreModule = CommandCoreModule()
		self.assertEqual(pCommandCoreModule.getModuleId(), 'core')
	# async def test_getModuleId(self)

	async def test_execute_activateModule_default(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=True)
		pModuleManager.deactivateModule = mock.Mock(return_value=True)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma'])
		expectedMessage = "@author Module 'karma' activated with access level 'user'!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('1')
		pModuleManager.activateModule.assert_called_once_with('channel', 'karma', 1)
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_default(self)

	async def test_execute_activateModule_failure_additionalArgument(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=False)
		pModuleManager.deactivateModule = mock.Mock(return_value=False)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', '5', 'kem1W'])
		expectedMessage = "@author Error activating module 'karma'!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('5')
		pModuleManager.activateModule.assert_called_once_with('channel', 'karma', 5)
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_failure_additionalArgument(self)

	async def test_execute_activateModule_failure_unknownUserLevel(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=False)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=False)
		pModuleManager.deactivateModule = mock.Mock(return_value=False)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', 'kem1W'])
		expectedMessage = "@author Error activating module 'karma', no access level 'kem1W' defined!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('kem1W')
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_failure_unknownUserLevel(self)

	async def test_execute_activateModule_success(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=True)
		pModuleManager.deactivateModule = mock.Mock(return_value=True)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', '5', 'kem1W'])
		expectedMessage = "@author Module 'karma' activated with access level 'sub'!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('5')
		pModuleManager.activateModule.assert_called_once_with('channel', 'karma', 5)
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_success(self)

	async def test_execute_activateModule_zero(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=True)
		pModuleManager.deactivateModule = mock.Mock(return_value=True)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', '0', 'kem1W'])
		expectedMessage = "@author Module 'karma' deactivated!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('0')
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_called_once_with('channel', 'karma')
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_zero(self)

	async def test_execute_deactivateModule_failure(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=False)
		pModuleManager.deactivateModule = mock.Mock(return_value=False)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['rem', 'karma', 'kem1W'])
		expectedMessage = "@author Error deactivating module 'karma'!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_called_once_with('channel', 'karma')
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_deactivateModule_failure(self)

	async def test_execute_deactivateModule_success(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=True)
		pModuleManager.deactivateModule = mock.Mock(return_value=True)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['rem', 'karma', 'kem1W'])
		expectedMessage = "@author Module 'karma' deactivated!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_called_once_with('channel', 'karma')
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_deactivateModule_success(self)

	async def test_execute_getModulesList(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=True)
		pModuleManager.deactivateModule = mock.Mock(return_value=True)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager
		pCommandCoreModule.pUserLevel = minidi.get(UserLevel)

		pMessage = Message(author=MessageAuthor(name='author'), channel=MessageChannel(name='channel'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['list', 'kem1W'])
		expectedMessage = "@author karma: -, mm: sub, score: user"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_called_once_with('channel')
	# async def test_execute_getModulesList(self)
# class TestCommandCoreModule(unittest.IsolatedAsyncioTestCase)