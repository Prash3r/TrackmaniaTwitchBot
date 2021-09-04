# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.Environment import Environment
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.logic.UserRights import UserRights
from TTBot.module.core.CommandCoreInvite import CommandCoreInvite

class TestUserRights(unittest.TestCase):
	def setUpEnvironment(self, botName: str) -> Environment:
		pEnvironment = Environment()
		pEnvironment.getTwitchBotUsername = mock.Mock(return_value=botName)

		return pEnvironment
	# def setUpEnvironment(self, botName: str) -> Environment

	def setUpMessageEvaluator(self, getUserLevel: int, isMainDevMessage: bool, isOwnerMessage: bool) -> MessageEvaluator:
		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.getUserLevel = mock.Mock(return_value=getUserLevel)
		pMessageEvaluator.isMainDeveloperMessage = mock.Mock(return_value=isMainDevMessage)
		pMessageEvaluator.isOwnerMessage = mock.Mock(return_value=isOwnerMessage)

		return pMessageEvaluator
	# def setUpMessageEvaluator(self, getUserLevel: int, isMainDevMessage: bool, isOwnerMessage: bool) -> MessageEvaluator

	def setUpModuleManager(self, minimumAccessLevel: int) -> ModuleManager:
		pModuleManager = ModuleManager()
		pModuleManager.getChannels = mock.Mock(return_value=['unittest'])
		pModuleManager.getMinimumAccessLevel = mock.Mock(return_value=minimumAccessLevel)

		return pModuleManager
	# def setUpModuleManager(self, minimumAccessLevel: int) -> ModuleManager

	def setUpUserRights(self, pEnvironment: Environment, pMessageEvaluator: MessageEvaluator, pModuleManager: ModuleManager) -> UserRights:
		pUserRights = UserRights()
		pUserRights.pEnvironment = pEnvironment
		pUserRights.pMessageEvaluator = pMessageEvaluator
		pUserRights.pModuleManager = pModuleManager

		return pUserRights
	# def setUpUserRights(self, pEnvironment: Environment, pMessageEvaluator: MessageEvaluator, pModuleManager: ModuleManager) -> UserRights

	def test_allowModuleExecution_allow(self):
		pEnvironment = self.setUpEnvironment(botName='trackmania_bot')
		pMessageEvaluator = self.setUpMessageEvaluator(getUserLevel=5, isMainDevMessage=False, isOwnerMessage=False)
		pModuleManager = self.setUpModuleManager(minimumAccessLevel=5)
		pUserRights = self.setUpUserRights(pEnvironment, pMessageEvaluator, pModuleManager)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pMessageEvaluator.isMainDeveloperMessage.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
		pModuleManager.getChannels.assert_called_once()
		pModuleManager.getMinimumAccessLevel.assert_called_once_with('unittest', 'core')
	# def test_allowModuleExecution_allow(self)

	def test_allowModuleExecution_botChannel(self):
		pEnvironment = self.setUpEnvironment(botName='trackmania_bot')
		pMessageEvaluator = self.setUpMessageEvaluator(getUserLevel=5, isMainDevMessage=False, isOwnerMessage=False)
		pModuleManager = self.setUpModuleManager(minimumAccessLevel=5)
		pUserRights = self.setUpUserRights(pEnvironment, pMessageEvaluator, pModuleManager)

		pMessage = Message(channel=MessageChannel(name='trackmania_bot'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isMainDeveloperMessage.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
		pModuleManager.getChannels.assert_not_called()
		pModuleManager.getMinimumAccessLevel.assert_not_called()
	# def test_allowModuleExecution_botChannel(self)
	
	def test_allowModuleExecution_disabled(self):
		pEnvironment = self.setUpEnvironment(botName='trackmania_bot')
		pMessageEvaluator = self.setUpMessageEvaluator(getUserLevel=5, isMainDevMessage=False, isOwnerMessage=False)
		pModuleManager = self.setUpModuleManager(minimumAccessLevel=0)
		pUserRights = self.setUpUserRights(pEnvironment, pMessageEvaluator, pModuleManager)

		pMessage = Message(channel=MessageChannel(name='notBotChannel'))
		pModule = CommandCoreInvite()
		self.assertRaises(RuntimeError, pUserRights.allowModuleExecution, pModule, pMessage)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isMainDeveloperMessage.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
		pModuleManager.getChannels.assert_called_once()
		pModuleManager.getMinimumAccessLevel.assert_not_called()
	# def test_allowModuleExecution_disabled(self)

	def test_allowModuleExecution_disallow(self):
		pEnvironment = self.setUpEnvironment(botName='trackmania_bot')
		pMessageEvaluator = self.setUpMessageEvaluator(getUserLevel=1, isMainDevMessage=False, isOwnerMessage=False)
		pModuleManager = self.setUpModuleManager(minimumAccessLevel=5)
		pUserRights = self.setUpUserRights(pEnvironment, pMessageEvaluator, pModuleManager)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)

		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pMessageEvaluator.isMainDeveloperMessage.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
		pModuleManager.getChannels.assert_called_once()
		pModuleManager.getMinimumAccessLevel.assert_called_once_with('unittest', 'core')
	# def test_allowModuleExecution_disallow(self)

	def test_allowModuleExecution_mainDevMessage(self):
		pEnvironment = self.setUpEnvironment(botName='trackmania_bot')
		pMessageEvaluator = self.setUpMessageEvaluator(getUserLevel=5, isMainDevMessage=True, isOwnerMessage=False)
		pModuleManager = self.setUpModuleManager(minimumAccessLevel=5)
		pUserRights = self.setUpUserRights(pEnvironment, pMessageEvaluator, pModuleManager)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isMainDeveloperMessage.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
		pModuleManager.getChannels.assert_not_called()
		pModuleManager.getMinimumAccessLevel.assert_not_called()
	# def test_allowModuleExecution_mainDevMessage(self)

	def test_allowModuleExecution_ownerMessage(self):
		pEnvironment = self.setUpEnvironment(botName='trackmania_bot')
		pMessageEvaluator = self.setUpMessageEvaluator(getUserLevel=5, isMainDevMessage=False, isOwnerMessage=True)
		pModuleManager = self.setUpModuleManager(minimumAccessLevel=5)
		pUserRights = self.setUpUserRights(pEnvironment, pMessageEvaluator, pModuleManager)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isMainDeveloperMessage.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
		pModuleManager.getChannels.assert_not_called()
		pModuleManager.getMinimumAccessLevel.assert_not_called()
	# def test_allowModuleExecution_ownerMessage(self)
# class TestUserRights(unittest.TestCase)