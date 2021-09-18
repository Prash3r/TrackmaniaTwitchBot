# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.ModuleManager import ModuleManager
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

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma'])
		expectedMessage = "@unittest Module 'karma' activated with access level 1!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_called_once_with('unittest', 'karma', 1)
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_default(self)

	async def test_execute_activateModule_failure(self):
		pInputSanitizer = InputSanitizer()
		pInputSanitizer.isInteger = mock.Mock(return_value=True)

		pModuleManager = ModuleManager()
		pModuleManager.activateModule = mock.Mock(return_value=False)
		pModuleManager.deactivateModule = mock.Mock(return_value=False)
		pModuleManager.listModulesForChannel = mock.Mock(return_value={'karma': 0, 'mm': 5, 'score': 1})

		pCommandCoreModule = CommandCoreModule()
		pCommandCoreModule.pInputSanitizer = pInputSanitizer
		pCommandCoreModule.pModuleManager = pModuleManager

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', '5', 'kem1W'])
		expectedMessage = "@unittest Error activating module 'karma'!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('5')
		pModuleManager.activateModule.assert_called_once_with('unittest', 'karma', 5)
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_not_called()
	# async def test_execute_activateModule_failure(self)

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

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', '5', 'kem1W'])
		expectedMessage = "@unittest Module 'karma' activated with access level 5!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('5')
		pModuleManager.activateModule.assert_called_once_with('unittest', 'karma', 5)
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

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['add', 'karma', '0', 'kem1W'])
		expectedMessage = "@unittest Module 'karma' deactivated!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_called_once_with('0')
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_called_once_with('unittest', 'karma')
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

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['rem', 'karma', 'kem1W'])
		expectedMessage = "@unittest Error deactivating module 'karma'!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_called_once_with('unittest', 'karma')
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

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['rem', 'karma', 'kem1W'])
		expectedMessage = "@unittest Module 'karma' deactivated!"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_called_once_with('unittest', 'karma')
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

		pMessage = Message(author=MessageAuthor(name='unittest'))
		actualMessage = await pCommandCoreModule.execute(pMessage, ['list', 'kem1W'])
		expectedMessage = "@unittest karma: 0, mm: 5, score: 1"
		self.assertEqual(actualMessage, expectedMessage)

		pInputSanitizer.isInteger.assert_not_called()
		pModuleManager.activateModule.assert_not_called()
		pModuleManager.deactivateModule.assert_not_called()
		pModuleManager.listModulesForChannel.assert_called_once_with('unittest')
	# async def test_execute_getModulesList(self)
# class TestCommandCoreModule(unittest.IsolatedAsyncioTestCase)