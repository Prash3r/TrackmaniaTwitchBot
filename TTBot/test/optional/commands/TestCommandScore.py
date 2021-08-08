# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.Randomizer import Randomizer
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.optional.commands.CommandScore import CommandScore

class TestCommandScore(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandString(self):
		pCommandScore = CommandScore()
		self.assertEqual(pCommandScore.getCommandString(), 'score')
	# async def test_getCommandString(self)

	async def test_getRightsId(self):
		pCommandScore = CommandScore()
		self.assertEqual(pCommandScore.getRightsId(), 'score')
	# async def test_getRightsId(self)

	async def test_execute_default(self):
		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=12345)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandScore = CommandScore()
		pCommandScore.pRandomizer = pRandomizer
		pCommandScore.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		result = await pCommandScore.execute(pMessage, 'unused')
		self.assertEqual(result, "@unittest has 12345 LP!")

		pRandomizer.uniformInt.assert_called_once_with(0, 100000)
		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_default(self)

	async def test_execute_special69(self):
		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=69)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandScore = CommandScore()
		pCommandScore.pRandomizer = pRandomizer
		pCommandScore.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		result = await pCommandScore.execute(pMessage, 'unused')
		self.assertEqual(result, "@unittest has 69 LP - nice!")

		pRandomizer.uniformInt.assert_called_once_with(0, 100000)
		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_special69(self)

	async def test_execute_special42069(self):
		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=42069)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandScore = CommandScore()
		pCommandScore.pRandomizer = pRandomizer
		pCommandScore.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		result = await pCommandScore.execute(pMessage, 'unused')
		self.assertEqual(result, "@unittest has 42069 LP - NICE!")

		pRandomizer.uniformInt.assert_called_once_with(0, 100000)
		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_special42069(self)

	async def test_execute_special69420(self):
		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=69420)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandScore = CommandScore()
		pCommandScore.pRandomizer = pRandomizer
		pCommandScore.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		result = await pCommandScore.execute(pMessage, 'unused')
		self.assertEqual(result, "@unittest has 69420 LP - MEGANICE!")

		pRandomizer.uniformInt.assert_called_once_with(0, 100000)
		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_special69420(self)

	async def test_execute_specialPart69(self):
		pRandomizer = Randomizer()
		pRandomizer.uniformInt = mock.Mock(return_value=52693)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandScore = CommandScore()
		pCommandScore.pRandomizer = pRandomizer
		pCommandScore.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		result = await pCommandScore.execute(pMessage, 'unused')
		self.assertEqual(result, "@unittest has 52693 LP - partly nice!")

		pRandomizer.uniformInt.assert_called_once_with(0, 100000)
		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_specialPart69(self)
# class TestCommandScore(unittest.IsolatedAsyncioTestCase)