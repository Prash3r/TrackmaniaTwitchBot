# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.logic.Randomizer import Randomizer
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.optional.commands.CommandJoke import CommandJoke

class TestCommandJoke(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandString(self):
		pCommandJoke = CommandJoke()
		self.assertEqual(pCommandJoke.getCommandString(), 'joke')
	# async def test_getCommandString(self)

	async def test_getRightsId(self):
		pCommandJoke = CommandJoke()
		self.assertEqual(pCommandJoke.getRightsId(), 'joke')
	# async def test_getRightsId(self)

	async def test_execute_default_randomDefault(self):
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
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "Fegir")

		pProcessVariables.get.assert_not_called()
		pProcessVariables.write.assert_not_called()

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_default_randomDefault(self)

	async def test_execute_default_randomSpecial(self):
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
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "modCheck .. unittest .. KEKW")

		pProcessVariables.get.assert_not_called()
		pProcessVariables.write.assert_not_called()

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_default_randomSpecial(self)

	async def test_execute_userAmaterasu_randomDefault(self):
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
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "you know who!")

		pProcessVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pProcessVariables.write.assert_called_once_with('lastjoker', 'amaterasutm')

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_userAmaterasu_randomDefault(self)

	async def test_execute_userAmaterasu_randomSpecial(self):
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
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "kem1W")

		pProcessVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pProcessVariables.write.assert_called_once_with('lastjoker', 'amaterasutm')

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_userAmaterasu_randomSpecial(self)

	async def test_execute_userFegir(self):
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
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "unittest")

		pProcessVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pProcessVariables.write.assert_called_once_with('lastjoker', 'fegir')

		pRandomizer.uniformFloat.assert_not_called()

		pTwitchMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute_userFegir(self)
# class TestCommandJoke(unittest.IsolatedAsyncioTestCase)