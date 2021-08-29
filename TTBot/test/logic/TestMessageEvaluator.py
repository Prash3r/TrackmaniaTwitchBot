# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.MessageEvaluator import MessageEvaluator

class TestMessageEvaluator(unittest.TestCase):
	def test_getAuthor(self):
		pAuthor = MessageAuthor(name='unittest')
		pMessage = Message(author=pAuthor)

		pMessageEvaluator = MessageEvaluator()
		pEvaluatedAuthor = pMessageEvaluator.getAuthor(pMessage)
		self.assertIs(pEvaluatedAuthor, pAuthor)
		self.assertEqual(pEvaluatedAuthor.getName(), 'unittest')
	# def test_getAuthor(self)

	def test_getAuthorName(self):
		pAuthor = MessageAuthor(name='unittest')
		pMessage = Message(author=pAuthor)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getAuthorName(pMessage), 'unittest')
	# def test_getAuthor(self)

	def test_getChannel(self):
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		pEvaluatedChannel = pMessageEvaluator.getChannel(pMessage)
		self.assertIs(pEvaluatedChannel, pChannel)
		self.assertEqual(pEvaluatedChannel.getName(), 'unittest')
	# def test_getChannel(self)

	def test_getChannelName(self):
		pChannel = MessageChannel(name='unittest')
		pMessage = Message(channel=pChannel)

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getChannelName(pMessage), 'unittest')
	# def test_getChannelName(self)

	def test_getContent(self):
		pMessage = Message(content='unittest')

		pMessageEvaluator = MessageEvaluator()
		self.assertEqual(pMessageEvaluator.getContent(pMessage), 'unittest')
	# def test_getContent(self)

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