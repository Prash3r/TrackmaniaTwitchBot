# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.Environment import Environment
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.UserRights import UserRights
from TTBot.optional.commands.core.CommandCoreInvite import CommandCoreInvite

class TestUserRights(unittest.TestCase):
	def setUpEnvironment(self, botName: str) -> Environment:
		pEnvironment = Environment()
		pEnvironment.getTwitchBotUsername = mock.Mock(return_value=botName)

		return pEnvironment
	# def setUpEnvironment(self, botName: str) -> Environment

	def setUpDbConnector(self, rows: list) -> DbConnector:
		pDbConnector = DbConnector()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		return pDbConnector
	# def setUpDbConnector(self, rows: list) -> DbConnector

	def setUpMessageEvaluator(self, getUserLevel: int, isOwnerMessage: bool) -> MessageEvaluator:
		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.getUserLevel = mock.Mock(return_value=getUserLevel)
		pMessageEvaluator.isOwnerMessage = mock.Mock(return_value=isOwnerMessage)

		return pMessageEvaluator
	# def setUpMessageEvaluator(self, getUserLevel: int, isOwnerMessage: bool) -> MessageEvaluator

	def setUpUserRights(self, pDbConnector: DbConnector, pEnvironment: Environment, pMessageEvaluator: MessageEvaluator) -> UserRights:
		pUserRights = UserRights()
		pUserRights.pDbConnector = pDbConnector
		pUserRights.pEnvironment = pEnvironment
		pUserRights.pMessageEvaluator = pMessageEvaluator

		return pUserRights
	# def setUpUserRights(self, pDbConnector: DbConnector, pEnvironment: Environment, pMessageEvaluator: MessageEvaluator) -> UserRights

	def test_allowModuleExecution_allow(self):
		pDbConnector = self.setUpDbConnector([{'core': 5}])
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pDbConnector, pEnvironment, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_allow(self)

	def test_allowModuleExecution_botChannel(self):
		pDbConnector = self.setUpDbConnector([{'core': 5}])
		pEnvironment = self.setUpEnvironment('unittest')
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pDbConnector, pEnvironment, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)

		pDbConnector.fetch.assert_not_called()
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_botChannel(self)
	
	def test_allowModuleExecution_disabled(self):
		pDbConnector = self.setUpDbConnector([{'core': 0}])
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pDbConnector, pEnvironment, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disabled(self)

	def test_allowModuleExecution_disallow(self):
		pDbConnector = self.setUpDbConnector([{'core': 5}])
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMessageEvaluator = self.setUpMessageEvaluator(1, False)
		pUserRights = self.setUpUserRights(pDbConnector, pEnvironment, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)

		pDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_called_once_with(pMessage)
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_disallow(self)

	def test_allowModuleExecution_ownerMessage(self):
		pDbConnector = self.setUpDbConnector([{'core': 5}])
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMessageEvaluator = self.setUpMessageEvaluator(5, True)
		pUserRights = self.setUpUserRights(pDbConnector, pEnvironment, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertTrue(allowModuleExecution)
		
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pDbConnector.fetch.assert_not_called()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_ownerMessage(self)

	def test_allowModuleExecution_queryEmpty(self):
		pDbConnector = self.setUpDbConnector([])
		pEnvironment = self.setUpEnvironment('notBotChannel')
		pMessageEvaluator = self.setUpMessageEvaluator(5, False)
		pUserRights = self.setUpUserRights(pDbConnector, pEnvironment, pMessageEvaluator)

		pMessage = Message(channel=MessageChannel(name='unittest'))
		pModule = CommandCoreInvite()
		allowModuleExecution = pUserRights.allowModuleExecution(pModule, pMessage)
		self.assertFalse(allowModuleExecution)
		
		pDbConnector.fetch.assert_called_once_with("SELECT `core` FROM `modules` WHERE `channel` = 'unittest' LIMIT 1;")
		pEnvironment.getTwitchBotUsername.assert_called_once()
		pMessageEvaluator.getUserLevel.assert_not_called()
		pMessageEvaluator.isOwnerMessage.assert_called_once_with(pMessage)
	# def test_allowModuleExecution_queryEmpty(self)
# class TestUserRights(unittest.TestCase)