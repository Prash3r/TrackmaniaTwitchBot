# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.module.Module import Module
from TTBot.module.ModuleList import ModuleList

class FalseModule(Module):
	def getModuleId(self) -> str:
		return 'false'
	
	async def onBotStartup(self) -> bool:
		return False
# class FalseModule(Module)

class MockModule(Module):
	def getModuleId(self) -> str:
		return 'mock'
# class MockModule(Module)

class TrueModule(Module):
	def getModuleId(self) -> str:
		return 'true'
	
	async def onBotStartup(self) -> bool:
		return True
# class TrueModule(Module)

class TestModuleCallbackRunner(unittest.IsolatedAsyncioTestCase):
	async def test_onBotStartup_Default(self):
		pModuleFactory = ModuleFactory()

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory

		success = await pModuleCallbackRunner.onBotStartup([])
		self.assertTrue(success)
	# async def test_onBotStartup_Default(self)

	async def test_onBotStartup_False(self):
		pModuleFactory = ModuleFactory()

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory

		success = await pModuleCallbackRunner.onBotStartup([FalseModule])
		self.assertFalse(success)
	# async def test_onBotStartup_False(self)

	async def test_onBotStartup_True(self):
		pModuleFactory = ModuleFactory()

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory

		success = await pModuleCallbackRunner.onBotStartup([TrueModule])
		self.assertTrue(success)
	# async def test_onBotStartup_True(self)

	async def test_onModuleEnable(self):
		pFalseModule = FalseModule()
		pFalseModule.onModuleEnable = mock.Mock()

		pMockModule = MockModule()
		pMockModule.onModuleEnable = mock.Mock()

		pTrueModule = TrueModule()
		pTrueModule.onModuleEnable = mock.Mock()

		pModuleFactory = ModuleFactory()
		pModuleFactory.createModule = mock.Mock(side_effect=[pFalseModule, pMockModule, pTrueModule])

		pModuleList = ModuleList()
		pModuleList.getModuleClasses = mock.Mock(return_value=[FalseModule, MockModule, TrueModule])

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory
		pModuleCallbackRunner.pModuleList = pModuleList
		pModuleCallbackRunner.onModuleEnable('mock')

		pFalseModule.onModuleEnable.assert_not_called()
		pMockModule.onModuleEnable.assert_called_once()
		pTrueModule.onModuleEnable.assert_not_called()
		pModuleFactory.createModule.assert_called()
		pModuleList.getModuleClasses.assert_called_once()
	# async def test_onModuleEnable(self)

	async def test_onModuleDisable(self):
		pFalseModule = FalseModule()
		pFalseModule.onModuleDisable = mock.Mock()

		pMockModule = MockModule()
		pMockModule.onModuleDisable = mock.Mock()

		pTrueModule = TrueModule()
		pTrueModule.onModuleDisable = mock.Mock()

		pModuleFactory = ModuleFactory()
		pModuleFactory.createModule = mock.Mock(side_effect=[pFalseModule, pMockModule, pTrueModule])

		pModuleList = ModuleList()
		pModuleList.getModuleClasses = mock.Mock(return_value=[FalseModule, MockModule, TrueModule])

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory
		pModuleCallbackRunner.pModuleList = pModuleList
		pModuleCallbackRunner.onModuleDisable('mock')

		pFalseModule.onModuleDisable.assert_not_called()
		pMockModule.onModuleDisable.assert_called_once()
		pTrueModule.onModuleDisable.assert_not_called()
		pModuleFactory.createModule.assert_called()
		pModuleList.getModuleClasses.assert_called_once()
	# async def test_onModuleDisable(self)
# class TestModuleCallbackRunner(unittest.TestCase)