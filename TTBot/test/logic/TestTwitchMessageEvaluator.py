# pylib
import unittest
from unittest import mock

# vendor
import twitchio

# local
from TTBot.logic.Environment import Environment
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator

class TestTwitchMessageEvaluator(unittest.TestCase):
	def test_getAuthor(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pEvaluatedAuthor = pTwitchMessageEvaluator.getAuthor(pMessage)
		self.assertEqual(pEvaluatedAuthor, pAuthor)
		self.assertEqual(pEvaluatedAuthor.name, 'unittest')
	# def test_getAuthor(self)

	def test_getAuthorName(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getAuthorName(pMessage), 'unittest')
	# def test_getAuthor(self)

	def test_getChannel(self):
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.channel = pChannel

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pEvaluatedChannel = pTwitchMessageEvaluator.getChannel(pMessage)
		self.assertEqual(pEvaluatedChannel, pChannel)
		self.assertEqual(pEvaluatedChannel.name, 'unittest')
	# def test_getChannel(self)

	def test_getChannelName(self):
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.channel = pChannel

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getChannelName(pMessage), 'unittest')
	# def test_getChannelName(self)

	def test_getContent(self):
		pMessage = mock.Mock(twitchio.Message)
		pMessage.content = 'unittest'

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getContent(pMessage), 'unittest')
	# def test_getContent(self)

	def test_getUserLevel_developer(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.is_mod = mock.Mock(return_value=False)
		pAuthor.is_subscriber = mock.Mock(return_value=False)
		pAuthor.name = 'PRASH3R'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getUserLevel(pMessage), 100)

		pAuthor.is_mod.assert_not_called()
		pAuthor.is_subscriber.assert_not_called()
	# def test_getUserLevel_developer(self)

	def test_getUserLevel_moderator(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.is_mod = mock.Mock(return_value=True)
		pAuthor.is_subscriber = mock.Mock(return_value=False)
		pAuthor.name = 'moderator'
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		pMessage.channel = pChannel

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getUserLevel(pMessage), 10)
		
		pAuthor.is_mod.assert_called_once()
		pAuthor.is_subscriber.assert_not_called()
	# def test_getUserLevel_moderator(self)

	def test_getUserLevel_owner(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.is_mod = mock.Mock(return_value=False)
		pAuthor.is_subscriber = mock.Mock(return_value=False)
		pAuthor.name = 'unittest'
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		pMessage.channel = pChannel

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getUserLevel(pMessage), 100)
		
		pAuthor.is_mod.assert_not_called()
		pAuthor.is_subscriber.assert_not_called()
	# def test_getUserLevel_owner(self)

	def test_getUserLevel_subscriber(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.is_mod = mock.Mock(return_value=False)
		pAuthor.is_subscriber = mock.Mock(return_value=True)
		pAuthor.name = 'subscriber'
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		pMessage.channel = pChannel

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getUserLevel(pMessage), 5)
		
		pAuthor.is_mod.assert_called_once()
		pAuthor.is_subscriber.assert_called_once()
	# def test_getUserLevel_subscriber(self)

	def test_getUserLevel_viewer(self):
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.is_mod = mock.Mock(return_value=False)
		pAuthor.is_subscriber = mock.Mock(return_value=False)
		pAuthor.name = 'viewer'
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		pMessage.channel = pChannel

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		self.assertEqual(pTwitchMessageEvaluator.getUserLevel(pMessage), 1)
		
		pAuthor.is_mod.assert_called_once()
		pAuthor.is_subscriber.assert_called_once()
	# def test_getUserLevel_viewer(self)

	def test_isBotAuthor(self):
		pEnvironment = Environment()
		pEnvironment.getTwitchBotUsername = mock.Mock(return_value='unittest')
		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.pEnvironment = pEnvironment
		
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		self.assertTrue(pTwitchMessageEvaluator.isBotAuthor(pMessage))
		
		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.name = 'viewer'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		self.assertFalse(pTwitchMessageEvaluator.isBotAuthor(pMessage))
	# def test_isBotAuthor(self)

	def test_isBotChannel(self):
		pEnvironment = Environment()
		pEnvironment.getTwitchBotUsername = mock.Mock(return_value='unittest')
		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.pEnvironment = pEnvironment
		
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.channel = pChannel
		self.assertTrue(pTwitchMessageEvaluator.isBotChannel(pMessage))
		
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'viewer'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.channel = pChannel
		self.assertFalse(pTwitchMessageEvaluator.isBotChannel(pMessage))
	# def test_isBotChannel(self)

	def test_isOwnerMessage(self):
		pTwitchMessageEvaluator = TwitchMessageEvaluator()

		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.name = 'UNITTEST'
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		pMessage.channel = pChannel
		self.assertTrue(pTwitchMessageEvaluator.isOwnerMessage(pMessage))

		pAuthor = mock.Mock(twitchio.Chatter)
		pAuthor.name = 'viewer'
		pChannel = mock.Mock(twitchio.Channel)
		pChannel.name = 'unittest'
		pMessage = mock.Mock(twitchio.Message)
		pMessage.author = pAuthor
		pMessage.channel = pChannel
		self.assertFalse(pTwitchMessageEvaluator.isOwnerMessage(pMessage))
	# def test_isOwnerMessage(self)
# class TestTwitchMessageEvaluator(unittest.TestCase)