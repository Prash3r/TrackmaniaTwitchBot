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
	
	def onBotStartup(self) -> bool:
		return False
# class FalseModule(Module)

class MockModule(Module):
	def getModuleId(self) -> str:
		return 'mock'
# class MockModule(Module)

class TrueModule(Module):
	def getModuleId(self) -> str:
		return 'true'
	
	def onBotStartup(self) -> bool:
		return True
# class TrueModule(Module)

class TestModuleCallbackRunner(unittest.TestCase):
	def test_onBotStartup_Default(self):
		pModuleFactory = ModuleFactory()

		pModuleList = ModuleList()
		pModuleList.getModuleClasses = mock.Mock(return_value=[])

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory
		pModuleCallbackRunner.pModuleList = pModuleList

		success = pModuleCallbackRunner.onBotStartup()
		self.assertTrue(success)

		pModuleList.getModuleClasses.assert_called_once()
	# def test_onBotStartup_Default(self)

	def test_onBotStartup_False(self):
		pModuleFactory = ModuleFactory()

		pModuleList = ModuleList()
		pModuleList.getModuleClasses = mock.Mock(return_value=[FalseModule])

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory
		pModuleCallbackRunner.pModuleList = pModuleList

		success = pModuleCallbackRunner.onBotStartup()
		self.assertFalse(success)

		pModuleList.getModuleClasses.assert_called_once()
	# def test_onBotStartup_False(self)

	def test_onBotStartup_True(self):
		pModuleFactory = ModuleFactory()

		pModuleList = ModuleList()
		pModuleList.getModuleClasses = mock.Mock(return_value=[TrueModule])

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.pModuleFactory = pModuleFactory
		pModuleCallbackRunner.pModuleList = pModuleList

		success = pModuleCallbackRunner.onBotStartup()
		self.assertTrue(success)

		pModuleList.getModuleClasses.assert_called_once()
	# def test_onBotStartup_True(self)

	def test_onModuleEnable(self):
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
	# def test_onModuleEnable(self)

	def test_onModuleDisable(self):
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
	# def test_onModuleDisable(self)
# class TestModuleCallbackRunner(unittest.TestCase)