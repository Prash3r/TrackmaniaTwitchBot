# pylib
import unittest

# local
from TTBot.logic.MessageSplitter import MessageSplitter

class TestMessageSplitter(unittest.TestCase):
	def test_split(self):
		pMessageSplitter = MessageSplitter()
		
		# priority check
		self.assertListEqual(
			pMessageSplitter.split('Hello, World!', ['o,', 'rl'], 10),
			['Hell', ' World!']
		)
		
		# normal
		self.assertListEqual(
			pMessageSplitter.split('Hello, World!', ['!', ', '], 10),
			['Hello', 'World!']
		)
		self.assertListEqual(
			pMessageSplitter.split('Hello, World!', ['!', ', '], 12),
			['Hello', 'World!']
		)
		
		# message short enough
		self.assertListEqual(
			pMessageSplitter.split('Hello, World!', ['!', ', '], 13),
			['Hello, World!']
		)

		# hard split
		self.assertListEqual(
			pMessageSplitter.split('Hello, World!', ['!', ', '], 5),
			['Hello', ', Wor', 'ld!']
		)
	# def test_split(self)

	def test__rindices(self):
		pMessageSplitter = MessageSplitter()
		self.assertListEqual(
			pMessageSplitter._rindices('abcde', ['d', 'cd', 'f']),
			[3, 2, -1]
		)
	# def test__rindices(self)

	def test__rindex(self):
		pMessageSplitter = MessageSplitter()
		self.assertEqual(pMessageSplitter._rindex('abcde',  'd'),  3)
		self.assertEqual(pMessageSplitter._rindex('abcde', 'cd'),  2)
		self.assertEqual(pMessageSplitter._rindex('abcde',  'f'), -1)
	# def test__rindex(self)
# class TestMessageSplitter(unittest.TestCase)