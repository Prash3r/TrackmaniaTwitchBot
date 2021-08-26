# pylib
from TTBot.optional.commands.core.CommandCoreInvite import CommandCoreInvite
import unittest
from unittest import mock

# local
from TTBot.logic.UserRights import UserRights

class TestUserRights(unittest.TestCase):
	def setUpMariaDbWrapper(self, rows: list) -> mock.Mock:
		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(return_value=rows)

		return pMariaDbWrapper
	# def setUpMariaDbWrapper(self, rows: list) -> mock.Mock

	def setUpTwitchMessageEvaluator(self, getUserLevel: int, isBotChannel: bool, isOwnerMessage: bool) -> mock.Mock:
		pTwitchMessageEvaluator = mock.Mock()
		pTwitchMessageEvaluator.getChannelName = mock.Mock(return_value='UnitTest')
		pTwitchMessageEvaluator.getUserLevel = mock.Mock(return_value=getUserLevel)
		pTwitchMessageEvaluator.isBotChannel = mock.Mock(return_value=isBotChannel)
		pTwitchMessageEvaluator.isOwnerMessage = mock.Mock(return_value=isOwnerMessage)

		return pTwitchMessageEvaluator
	# def setUpTwitchMessageEvaluator(self, getUserLevel: int, isBotChannel: bool, isOwnerMessage: bool) -> mock.Mock

	def setUpUserRights(self, pMariaDbWrapper: mock.Mock, pTwitchMessageEvaluator: mock.Mock) -> UserRights:
		pUserRights = UserRights()
		pUserRights.pMariaDbWrapper = pMariaDbWrapper
		pUserRights.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		return pUserRights
	# def setUpUserRights(self, pMariaDbWrapper: mock.Mock, pTwitchMessageEvaluator: mock.Mock) -> UserRights

	def test_allowModuleExecution_allow(self):
		pMariaDbWrapper = self.setUpMariaDbWrapper([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pMariaDbWrapper.fetch.assert_called_once_with("SELECT core FROM modules WHERE channel = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_allow(self)

	def test_allowModuleExecution_botChannel(self):
		pMariaDbWrapper = self.setUpMariaDbWrapper([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, True, False)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pMariaDbWrapper.fetch.assert_not_called()
		pTwitchMessageEvaluator.getChannelName.assert_not_called()
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_botChannel(self)
	
	def test_allowModuleExecution_disabled(self):
		pMariaDbWrapper = self.setUpMariaDbWrapper([{'core': 0}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT core FROM modules WHERE channel = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disabled(self)

	def test_allowModuleExecution_disallow(self):
		pMariaDbWrapper = self.setUpMariaDbWrapper([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(1, False, False)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)

		pMariaDbWrapper.fetch.assert_called_once_with("SELECT core FROM modules WHERE channel = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disallow(self)

	def test_allowModuleExecution_ownerMessage(self):
		pMariaDbWrapper = self.setUpMariaDbWrapper([{'core': 5}])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, True)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()

		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)
		
		pMariaDbWrapper.fetch.assert_not_called()
		pTwitchMessageEvaluator.getChannelName.assert_not_called()
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_ownerMessage(self)

	def test_allowModuleExecution_queryEmpty(self):
		pMariaDbWrapper = self.setUpMariaDbWrapper([])
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()

		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT core FROM modules WHERE channel = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_queryEmpty(self)

	def test_allowModuleExecution_queryError(self):
		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(side_effect=Exception(''))
		pTwitchMessageEvaluator = self.setUpTwitchMessageEvaluator(5, False, False)
		pUserRights = self.setUpUserRights(pMariaDbWrapper, pTwitchMessageEvaluator)

		pMessage = object()
		pModule = CommandCoreInvite()

		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT core FROM modules WHERE channel = 'unittest' LIMIT 1;")
		pTwitchMessageEvaluator.getChannelName.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.getUserLevel.assert_not_called()
		pTwitchMessageEvaluator.isBotChannel.assert_called_once_with(pMessage)
		pTwitchMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_queryError(self)
# class TestUserRights(unittest.TestCase)