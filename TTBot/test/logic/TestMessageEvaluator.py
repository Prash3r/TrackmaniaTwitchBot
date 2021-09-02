# pylib
import unittest

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.Developers import Developers
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.UserLevel import UserLevel

class TestMessageEvaluator(unittest.TestCase):
	def test_getUserLevel_developer(self):
		pAuthor = MessageAuthor(name='prash3r')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = Developers()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), UserLevel.ADMIN)
	# def test_getUserLevel_developer(self)

	def test_getUserLevel_moderator(self):
		pAuthor = MessageAuthor(isMod=True, name='moderator')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = Developers()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), UserLevel.MOD)
	# def test_getUserLevel_moderator(self)

	def test_getUserLevel_owner(self):
		pAuthor = MessageAuthor(name='unittest')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = Developers()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), UserLevel.ADMIN)
	# def test_getUserLevel_owner(self)

	def test_getUserLevel_subscriber(self):
		pAuthor = MessageAuthor(isSubscriber=True, name='subscriber')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = Developers()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), UserLevel.SUB)
	# def test_getUserLevel_subscriber(self)

	def test_getUserLevel_viewer(self):
		pAuthor = MessageAuthor(name='viewer')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = Developers()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), UserLevel.USER)
	# def test_getUserLevel_viewer(self)

	def test_isAtleastModMessage(self):
		pDevelopers = Developers()
		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = pDevelopers

		pAuthor = MessageAuthor(name='unittest')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)
		self.assertTrue(pMessageEvaluator.isAtleastModMessage(pMessage))

		mainDevelopers = pDevelopers.getMainDevelopers()
		for developer in mainDevelopers:
			pAuthor = MessageAuthor(name=developer)
			pMessage = Message(author=pAuthor, channel=pChannel)
			self.assertTrue(pMessageEvaluator.isAtleastModMessage(pMessage))
		# for developer in mainDevelopers

		moduleDevelopers = pDevelopers.getModuleDevelopers()
		for developer in moduleDevelopers:
			pAuthor = MessageAuthor(name=developer)
			pMessage = Message(author=pAuthor, channel=pChannel)
			self.assertFalse(pMessageEvaluator.isAtleastModMessage(pMessage))
		# for developer in moduleDevelopers
	# def test_isMainDeveloperMessage(self)

	def test_isMainDeveloperMessage(self):
		pDevelopers = Developers()
		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = pDevelopers

		pAuthor = MessageAuthor(name='unittest')
		pMessage = Message(author=pAuthor)
		self.assertFalse(pMessageEvaluator.isMainDeveloperMessage(pMessage))

		mainDevelopers = pDevelopers.getMainDevelopers()
		for developer in mainDevelopers:
			pAuthor = MessageAuthor(name=developer)
			pMessage = Message(author=pAuthor)
			self.assertTrue(pMessageEvaluator.isMainDeveloperMessage(pMessage))
		# for developer in mainDevelopers

		moduleDevelopers = pDevelopers.getModuleDevelopers()
		for developer in moduleDevelopers:
			pAuthor = MessageAuthor(name=developer)
			pMessage = Message(author=pAuthor)
			self.assertFalse(pMessageEvaluator.isMainDeveloperMessage(pMessage))
		# for developer in moduleDevelopers
	# def test_isMainDeveloperMessage(self)

	def test_isOwnerMessage(self):
		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.pDevelopers = Developers()

		pAuthor = MessageAuthor(name='UNITTEST')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)
		self.assertTrue(pMessageEvaluator.isOwnerMessage(pMessage))

		pAuthor = MessageAuthor(name='viewer')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)
		self.assertFalse(pMessageEvaluator.isOwnerMessage(pMessage))
	# def test_isOwnerMessage(self)
# class TestMessageEvaluator(unittest.TestCase)