# pylib
import os
import unittest

# local
from TTBot.logic.Environment import Environment

class TestEnvironment(unittest.TestCase):
	def test_getVariable(self):
		pEnvironment = Environment()
		self.assertRaises(EnvironmentError, pEnvironment.getVariable, 'Hello')

		os.environ['Hello'] = 'World'
		self.assertEqual(pEnvironment.getVariable('Hello'), 'World')
		self.assertRaises(EnvironmentError, pEnvironment.getVariable, 'World')
	# def test_getVariable(self)

	def test_getVariableWithDefault(self):
		pEnvironment = Environment()
		self.assertEqual(pEnvironment.getVariableWithDefault('Hello2', 'Tests2'), 'Tests2')

		os.environ['Hello2'] = 'World2'
		self.assertEqual(pEnvironment.getVariableWithDefault('Hello2', 'Tests2'), 'World2')
		self.assertEqual(pEnvironment.getVariableWithDefault('World2', 'Hello2'), 'Hello2')
	# def test_getVariableWithDefault(self)

	def test_getTwitchBotUsername(self):
		pEnvironment = Environment()
		self.assertRaises(EnvironmentError, pEnvironment.getTwitchBotUsername)

		os.environ['TWITCH_BOT_USERNAME'] = 'TwitchBotUsername'
		self.assertEqual(pEnvironment.getTwitchBotUsername(), 'twitchbotusername')
	# def test_getTwitchBotUsername(self)

	def test_isDebug(self):
		pEnvironment = Environment()
		self.assertTrue(pEnvironment.isDebug())

		os.environ['DEBUG'] = 'True'
		self.assertTrue(pEnvironment.isDebug())

		os.environ['DEBUG'] = 'bla'
		self.assertFalse(pEnvironment.isDebug())
	# def test_isDebug(self)
# class TestEnvironment(unittest.TestCase)