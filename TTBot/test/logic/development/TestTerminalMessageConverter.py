# pylib
import unittest

# local
from TTBot.logic.development.TerminalMessageConverter import TerminalMessageConverter

class TestTerminalMessageConverter(unittest.TestCase):
	def test_convert(self):
		pTerminalMessageConverter = TerminalMessageConverter()
		pMessage = pTerminalMessageConverter.convert('Hello, World!')
		
		self.assertEqual(pMessage.getAuthor().getName(), 'terminal')
		self.assertTrue(pMessage.getAuthor().isMod())
		self.assertTrue(pMessage.getAuthor().isSubscriber())

		self.assertEqual(pMessage.getChannel().getName(), 'terminal')

		self.assertEqual(pMessage.getContent(), 'Hello, World!')
	# def test_convert(self)
# class TestTerminalMessageConverter(unittest.TestCase)