# pylib
import unittest

# local
from TTBot.data.MessageAuthor import MessageAuthor

class TestMessageAuthor(unittest.TestCase):
	def test_default(self):
		pAuthor = MessageAuthor()
		self.assertEqual(pAuthor.getName(), '')
		self.assertFalse(pAuthor.isMod())
		self.assertFalse(pAuthor.isSubscriber())
	# def test_default(self)

	def test_filled(self):
		pAuthor = MessageAuthor(isMod=True, isSubscriber=True, name='Naxanria')
		self.assertEqual(pAuthor.getName(), 'Naxanria')
		self.assertTrue(pAuthor.isMod())
		self.assertTrue(pAuthor.isSubscriber())
	# def test_filled(self)
# class TestMessageAuthor(unittest.TestCase)