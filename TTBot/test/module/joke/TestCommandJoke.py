# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.Randomizer import Randomizer
from TTBot.module.joke.CommandJoke import CommandJoke

class TestCommandJoke(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandString(self):
		pCommandJoke = CommandJoke()
		self.assertEqual(pCommandJoke.getCommandString(), 'joke')
	# async def test_getCommandString(self)

	async def test_getModuleId(self):
		pCommandJoke = CommandJoke()
		self.assertEqual(pCommandJoke.getModuleId(), 'joke')
	# async def test_getModuleId(self)

	async def test_execute_default_randomDefault(self):
		pGlobalVariables = GlobalVariables()
		pGlobalVariables.get = mock.Mock()
		pGlobalVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.8)

		pCommandJoke = CommandJoke()
		pCommandJoke.pGlobalVariables = pGlobalVariables
		pCommandJoke.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "Fegir")

		pGlobalVariables.get.assert_not_called()
		pGlobalVariables.write.assert_not_called()

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)
	# async def test_execute_default_randomDefault(self)

	async def test_execute_default_randomSpecial(self):
		pGlobalVariables = GlobalVariables()
		pGlobalVariables.get = mock.Mock()
		pGlobalVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.9)

		pCommandJoke = CommandJoke()
		pCommandJoke.pGlobalVariables = pGlobalVariables
		pCommandJoke.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "modCheck .. unittest .. KEKW")

		pGlobalVariables.get.assert_not_called()
		pGlobalVariables.write.assert_not_called()

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)
	# async def test_execute_default_randomSpecial(self)

	async def test_execute_userAmaterasu_randomDefault(self):
		pGlobalVariables = GlobalVariables()
		pGlobalVariables.get = mock.Mock(return_value='unittest')
		pGlobalVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.8)

		pCommandJoke = CommandJoke()
		pCommandJoke.pGlobalVariables = pGlobalVariables
		pCommandJoke.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='amaterasutm'))
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "you know who!")

		pGlobalVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pGlobalVariables.write.assert_called_once_with('lastjoker', 'amaterasutm')

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)
	# async def test_execute_userAmaterasu_randomDefault(self)

	async def test_execute_userAmaterasu_randomSpecial(self):
		pGlobalVariables = GlobalVariables()
		pGlobalVariables.get = mock.Mock(return_value='unittest')
		pGlobalVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock(return_value=0.9)

		pCommandJoke = CommandJoke()
		pCommandJoke.pGlobalVariables = pGlobalVariables
		pCommandJoke.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='amaterasutm'))
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "kem1W")

		pGlobalVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pGlobalVariables.write.assert_called_once_with('lastjoker', 'amaterasutm')

		pRandomizer.uniformFloat.assert_called_once_with(0., 1.)
	# async def test_execute_userAmaterasu_randomSpecial(self)

	async def test_execute_userFegir(self):
		pGlobalVariables = GlobalVariables()
		pGlobalVariables.get = mock.Mock(return_value='unittest')
		pGlobalVariables.write = mock.Mock()

		pRandomizer = Randomizer()
		pRandomizer.uniformFloat = mock.Mock()

		pCommandJoke = CommandJoke()
		pCommandJoke.pGlobalVariables = pGlobalVariables
		pCommandJoke.pRandomizer = pRandomizer

		pMessage = Message(author=MessageAuthor(name='fegir'))
		result = await pCommandJoke.execute(pMessage, 'unused')
		self.assertEqual(result, "unittest")

		pGlobalVariables.get.assert_called_once_with('lastjoker', 'fegir')
		pGlobalVariables.write.assert_called_once_with('lastjoker', 'fegir')

		pRandomizer.uniformFloat.assert_not_called()
	# async def test_execute_userFegir(self)
# class TestCommandJoke(unittest.IsolatedAsyncioTestCase)