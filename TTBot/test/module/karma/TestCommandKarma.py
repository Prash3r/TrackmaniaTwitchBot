# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.module.karma.CommandKarma import CommandKarma

class TestCommandKarma(unittest.IsolatedAsyncioTestCase):
	async def _test_execute_display(self, isAtleastModMessage: bool, messageContent: str, commmandArgs: list):
		pInputSanitizer = InputSanitizer()

		pLocalVariables = LocalVariables()
		pLocalVariables.get = mock.Mock(return_value=69)
		pLocalVariables.write = mock.Mock()

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.isAtleastModMessage = mock.Mock(return_value=isAtleastModMessage)

		pCommandKarma = CommandKarma()
		pCommandKarma.pInputSanitizer = pInputSanitizer
		pCommandKarma.pLocalVariables = pLocalVariables
		pCommandKarma.pMessageEvaluator = pMessageEvaluator

		pChannel = MessageChannel(name='unittest')
		pMessage = Message(channel=pChannel, content=messageContent)

		message = await pCommandKarma.execute(pMessage, commmandArgs)
		self.assertEqual(message, "Current streamer karma: 69")

		pLocalVariables.get.assert_called_once_with('karma', 'unittest', 0)
		pLocalVariables.write.assert_not_called()
		pMessageEvaluator.isAtleastModMessage.assert_called_with(pMessage)
	# async def _test_execute_display(self, isAtleastModMessage: bool, messageContent: str, commmandArgs: list)

	async def test_execute_display_mod(self):
		await self._test_execute_display(isAtleastModMessage=True, messageContent='!karma', commmandArgs=[])

	async def test_execute_display_user(self):
		await self._test_execute_display(isAtleastModMessage=False, messageContent='!karma', commmandArgs=[])

	async def test_execute_setInt_user(self):
		await self._test_execute_display(isAtleastModMessage=False, messageContent='!karma 420', commmandArgs=['420'])

	async def test_execute_setString_mod(self):
		await self._test_execute_display(isAtleastModMessage=True, messageContent='!karma YEP', commmandArgs=['YEP'])

	async def test_execute_setString_user(self):
		await self._test_execute_display(isAtleastModMessage=False, messageContent='!karma YEP', commmandArgs=['YEP'])


	async def test_execute_setInt_mod(self):
		pInputSanitizer = InputSanitizer()

		pLocalVariables = LocalVariables()
		pLocalVariables.get = mock.Mock(return_value=69)
		pLocalVariables.write = mock.Mock()

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.isAtleastModMessage = mock.Mock(return_value=True)

		pCommandKarma = CommandKarma()
		pCommandKarma.pInputSanitizer = pInputSanitizer
		pCommandKarma.pLocalVariables = pLocalVariables
		pCommandKarma.pMessageEvaluator = pMessageEvaluator

		pChannel = MessageChannel(name='unittest')
		pMessage = Message(channel=pChannel, content='!karma 420')

		message = await pCommandKarma.execute(pMessage, ['420'])
		self.assertEqual(message, "Successfully changed karma, current streamer karma: 420")

		pLocalVariables.get.assert_not_called()
		pLocalVariables.write.assert_called_once_with('karma', 'unittest', 420)
		pMessageEvaluator.isAtleastModMessage.assert_called_with(pMessage)
	# async def test_execute_setInt_mod(self)
# class TestCommandKarma(unittest.IsolatedAsyncioTestCase)