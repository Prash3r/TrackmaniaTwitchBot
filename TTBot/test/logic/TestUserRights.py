# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.MariaDbConnector import MariaDbConnector
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.logic.UserRights import UserRights
from TTBot.optional.commands.core.CommandCoreInvite import CommandCoreInvite

class TestUserRights(unittest.TestCase):
	def setUpMariaDbConnector(self, rows: list) -> MariaDbConnector:
		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)

		return pMariaDbConnector
	# def setUpMariaDbConnector(self, rows: list) -> MariaDbConnector

	def setUpTwitchMessageEvaluator(self, getUserLevel: int, isBotChannel: bool, isOwnerMessage: bool) -> TwitchMessageEvaluator:
		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getChannelName = mock.Mock(return_value='UnitTest')
		pTwitchMessageEvaluator.getUserLevel = mock.Mock(return_value=getUserLevel)
		pTwitchMessageEvaluator.isBotChannel = mock.Mock(return_value=isBotChannel)
		pTwitchMessageEvaluator.isOwnerMessage = mock.Mock(return_value=isOwnerMessage)

		return pTwitchMessageEvaluator
	# def setUpTwitchMessageEvaluator(self, getUserLevel: int, isBotChannel: bool, isOwnerMessage: bool) -> TwitchMessageEvaluator

	def setUpUserRights(self, pMariaDbConnector: MariaDbConnector, pTwitchMessageEvaluator: TwitchMessageEvaluator) -> UserRights:
		pUserRights = UserRights()
		pUserRights.pMariaDbConnector = pMariaDbConnector
		pUserRights.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		return pUserRights
	# def setUpUserRights(self, pMariaDbConnector: MariaDbConnector, pTwitchMessageEvaluator: TwitchMessageEvaluator) -> UserRights

	def test_allowModuleExecution_allow(self):
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbConnector, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_allow(self)

	def test_allowModuleExecution_botChannel(self):
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, True, False)
		pUserRights = self.setUpUserRights(pMariaDbConnector, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pMariaDbConnector.fetch.assert_not_called()
		pTwitchMessageEvaluator.getChannelName.assert_not_called()
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_botChannel(self)
	
	def test_allowModuleExecution_disabled(self):
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 0}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbConnector, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disabled(self)

	def test_allowModuleExecution_disallow(self):
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(1, False, False)
		pUserRights = self.setUpUserRights(pMariaDbConnector, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)

		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disallow(self)

	def test_allowModuleExecution_ownerMessage(self):
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, True)
		pUserRights = self.setUpUserRights(pMariaDbConnector, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()

		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)
		
		pMariaDbConnector.fetch.assert_not_called()
		pTwitchMessageEvaluator.getChannelName.assert_not_called()
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_ownerMessage(self)

	def test_allowModuleExecution_queryEmpty(self):
		pMariaDbConnector = self.setUpMariaDbConnector([])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbConnector, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()

		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_queryEmpty(self)
# class TestUserRights(unittest.TestCase)