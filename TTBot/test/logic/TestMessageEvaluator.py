# pylib
import unittest

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.MessageEvaluator import MessageEvaluator

class TestMessageEvaluator(unittest.TestCase):
	def test_getUserLevel_developer(self):
		pAuthor = MessageAuthor(name='PRASH3R')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), 100)
	# def test_getUserLevel_developer(self)

	def test_getUserLevel_moderator(self):
		pAuthor = MessageAuthor(isMod=True, name='moderator')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), 10)
	# def test_getUserLevel_moderator(self)

	def test_getUserLevel_owner(self):
		pAuthor = MessageAuthor(name='unittest')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), 100)
	# def test_getUserLevel_owner(self)

	def test_getUserLevel_subscriber(self):
		pAuthor = MessageAuthor(isSubscriber=True, name='subscriber')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), 5)
	# def test_getUserLevel_subscriber(self)

	def test_getUserLevel_viewer(self):
		pAuthor = MessageAuthor(name='viewer')
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(author=pAuthor, channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getUserLevel(pMessage), 1)
	# def test_getUserLevel_viewer(self)

	def test_isOwnerMessage(self):
		pMessageEvaluator = MessageEvaluator()

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