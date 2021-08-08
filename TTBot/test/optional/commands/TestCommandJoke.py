# pylib
import asyncio
import unittest
from unittest import mock

# local
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.Randomizer import Randomizer
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.optional.commands.CommandJoke import CommandJoke

class TestCommandJoke(unittest.TestCase):
	def test_getCommandString(self):
		pCommandJoke = CommandJoke()
		self.assertEqual(pCommandJoke.getCommandString(), 'joke')
	# def test_getCommandString(self)

	def test_getRightsId(self):
		pCommandJoke = CommandJoke()
		self.assertEqual(pCommandJoke.getRightsId(), 'joke')
	# def test_getRightsId(self)

	def runTestExecute(self, pCommandJoke: CommandJoke, pMessage: object, result: str):
		loop = asyncio.get_event_loop()
		pCoroutine = pCommandJoke.execute(pMessage, 'unused')
		resultCoroutine = loop.run_until_complete(asyncio.gather(pCoroutine))
		self.assertEqual(resultCoroutine[0], result)
	# def runTestExecute(self, pCommandJoke: CommandJoke, result: str)

	def test_execute_default_randomDefault(self):
		pProcessVariables = ProcessVariables()
		pProcessVariables.get = mock.Mock()
		pProcessVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.8)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandJoke = CommandJoke()
		pCommandJoke.pProcessVariables = pProcessVariables
		pCommandJoke.pRandomizer = pRandomizer
		pCommandJoke.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		self.runTestExecute(pCommandJoke, pMessage, "Fegir")

		pProcessVariables.get.assert_not_called()
		pProcessVariables.write.assert_not_called()

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# def test_execute_default_randomDefault(self)

	def test_execute_default_randomSpecial(self):
		pProcessVariables = ProcessVariables()
		pProcessVariables.get = mock.Mock()
		pProcessVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.9)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pCommandJoke = CommandJoke()
		pCommandJoke.pProcessVariables = pProcessVariables
		pCommandJoke.pRandomizer = pRandomizer
		pCommandJoke.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		self.runTestExecute(pCommandJoke, pMessage, "modCheck .. unittest .. KEKW")

		pProcessVariables.get.assert_not_called()
		pProcessVariables.write.assert_not_called()

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# def test_execute_default_randomSpecial(self)

	def test_execute_userAmaterasu_randomDefault(self):
		pProcessVariables = ProcessVariables()
		pProcessVariables.get = mock.Mock(return_value='unittest')
		pProcessVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.8)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='amaterasutm')

		pCommandJoke = CommandJoke()
		pCommandJoke.pProcessVariables = pProcessVariables
		pCommandJoke.pRandomizer = pRandomizer
		pCommandJoke.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		self.runTestExecute(pCommandJoke, pMessage, "you know who!")

		pProcessVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pProcessVariables.write.assert_called_once_with('lastjoker', 'amaterasutm')

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# def test_execute_userAmaterasu_randomDefault(self)

	def test_execute_userAmaterasu_randomSpecial(self):
		pProcessVariables = ProcessVariables()
		pProcessVariables.get = mock.Mock(return_value='unittest')
		pProcessVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.9)

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='amaterasutm')

		pCommandJoke = CommandJoke()
		pCommandJoke.pProcessVariables = pProcessVariables
		pCommandJoke.pRandomizer = pRandomizer
		pCommandJoke.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		self.runTestExecute(pCommandJoke, pMessage, "kem1W")

		pProcessVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pProcessVariables.write.assert_called_once_with('lastjoker', 'amaterasutm')

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# def test_execute_userAmaterasu_randomSpecial(self)

	def test_execute_userFegir(self):
		pProcessVariables = ProcessVariables()
		pProcessVariables.get = mock.Mock(return_value='unittest')
		pProcessVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock()

		pTwitchMessageEvaluator = TwitchMessageEvaluator()
		pTwitchMessageEvaluator.getAuthorName = mock.Mock(return_value='fegir')

		pCommandJoke = CommandJoke()
		pCommandJoke.pProcessVariables = pProcessVariables
		pCommandJoke.pRandomizer = pRandomizer
		pCommandJoke.pTwitchMessageEvaluator = pTwitchMessageEvaluator

		pMessage = object()
		self.runTestExecute(pCommandJoke, pMessage, "unittest")

		pProcessVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pProcessVariables.write.assert_called_once_with('lastjoker', 'fegir')

		pRandomizer.uniformFloat.assert_not_called()

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# def test_execute_userFegir(self)
# class TestCommandJoke(unittest.TestCase)