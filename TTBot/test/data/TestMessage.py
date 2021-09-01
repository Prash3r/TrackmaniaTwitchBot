# pylib
import unittest

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.data.MessageChannel import MessageChannel

class TestMessage(unittest.TestCase):
	def test_default(self):
		pMessage = Message()
		self.assertIsNone(pMessage.getAuthor())
		self.assertIsNone(pMessage.getChannel())
		self.assertEqual(pMessage.getContent(), '')
	# def test_default(self)

	def test_filled(self):
		pAuthor = MessageAuthor(isMod=True, isSubscriber=False, name='dhofy')
		pChannel = MessageChannel(name='unittest')

		pMessage = Message(author=pAuthor, channel=pChannel, content='YEP COCK')

		self.assertIs(pMessage.getAuthor(), pAuthor)
		self.assertEqual(pMessage.getAuthor().getName(), 'dhofy')
		self.assertTrue(pMessage.getAuthor().isMod())
		self.assertFalse(pMessage.getAuthor().isSubscriber())

		self.assertIs(pMessage.getChannel(), pChannel)
		self.assertEqual(pMessage.getChannel().getName(), 'unittest')

		self.assertEqual(pMessage.getContent(), 'YEP COCK')
	# def test_filled(self)
# class TestMessage(unittest.TestCase)