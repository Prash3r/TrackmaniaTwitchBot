# pylib
import unittest

# local
from TTBot.data.MessageChannel import MessageChannel

class TestMessageChannel(unittest.TestCase):
	def test_default(self):
		pChannel = MessageChannel()
		self.assertEqual(pChannel.getName(), '')
	# def test_default(self)

	def test_filled(self):
		pAuthor = MessageChannel(name='unittest')
		self.assertEqual(pAuthor.getName(), 'unittest')
	# def test_filled(self)
# class TestMessageAuthor(unittest.TestCase)