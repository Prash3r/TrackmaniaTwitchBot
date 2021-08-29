# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.Environment import Environment
from TTBot.logic.MariaDbConnector import MariaDbConnector
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.UserRights import UserRights
from TTBot.optional.commands.core.CommandCoreInvite import CommandCoreInvite

class TestUserRights(unittest.TestCase):
	def setUpEnvironment(self, botName: str) -> Environment:
		pEnvironment = Environment()
		pEnvironment.getTwitchBotUsername = mock.Mock(return_value=botName)

		return pEnvironment
	# def setUpEnvironment(self, botName: str) -> Environment

	def setUpMariaDbConnector(self, rows: list) -> MariaDbConnector:
		pMariaDbConnector = MariaDbConnector()
		pMariaDbConnector.fetch = mock.Mock(return_value=rows)

		return pMariaDbConnector
	# def setUpMariaDbConnector(self, rows: list) -> MariaDbConnector

	def setUpMessageEvaluator(self, getUserLevel: int, isOwnerMessage: bool) -> MessageEvaluator:
		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.getUserLevel = mock.Mock(return_value=getUserLevel)
		pMessageEvaluator.isOwnerMessage = mock.Mock(return_value=isOwnerMessage)

		return pMessageEvaluator
	# def setUpMessageEvaluator(self, getUserLevel: int, isOwnerMessage: bool) -> MessageEvaluator

	def setUpUserRights(self, pEnvironment: Environment, pMariaDbConnector: MariaDbConnector, pMessageEvaluator: MessageEvaluator) -> UserRights:
		pUserRights = UserRights()
		pUserRights.pEnvironment = pEnvironment
		pUserRights.pMariaDbConnector = pMariaDbConnector
		pUserRights.pMessageEvaluator = pMessageEvaluator

		return pUserRights
	# def setUpUserRights(self, pEnvironment: Environment, pMariaDbConnector: MariaDbConnector, pMessageEvaluator: MessageEvaluator) -> UserRights

	def test_allowModuleExecution_allow(self):
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pEnvironment, pMariaDbConnector, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_allow(self)

	def test_allowModuleExecution_botChannel(self):
		pEnvironment = self.setUpEnvironment('unittest')
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pEnvironment, pMariaDbConnector, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMariaDbConnector.fetch.assert_not_called()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_botChannel(self)
	
	def test_allowModuleExecution_disabled(self):
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 0}])
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pEnvironment, pMariaDbConnector, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disabled(self)

	def test_allowModuleExecution_disallow(self):
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pMessageEvaluator = self.setUpMessageEvaluator(1, False)
		pUserRights = self.setUpUserRights(pEnvironment, pMariaDbConnector, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)

		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disallow(self)

	def test_allowModuleExecution_ownerMessage(self):
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMariaDbConnector = self.setUpMariaDbConnector([{'core': 5}])
		pMessageEvaluator = self.setUpMessageEvaluator(5, True)
		pUserRights = self.setUpUserRights(pEnvironment, pMariaDbConnector, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMariaDbConnector.fetch.assert_not_called()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_ownerMessage(self)

	def test_allowModuleExecution_queryEmpty(self):
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMariaDbConnector = self.setUpMariaDbConnector([])
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pEnvironment, pMariaDbConnector, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMariaDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_queryEmpty(self)
# class TestUserRights(unittest.TestCase)