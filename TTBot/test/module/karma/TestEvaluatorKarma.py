# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.module.karma.EvaluatorKarma import EvaluatorKarma

class TestEvaluatorKarma(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		pEvaluatorKarma = EvaluatorKarma()
		regex = pEvaluatorKarma.getMessageRegex()
		self.assertRegex("--", regex)
		self.assertRegex("-- it is", regex)
		self.assertRegex("That's a --", regex)
		self.assertRegex("YEP -- YEP", regex)
		self.assertRegex("++", regex)
		self.assertRegex("++ it is", regex)
		self.assertRegex("That's a ++", regex)
		self.assertRegex("YEP ++ YEP", regex)
		self.assertRegex("++ --", regex)
		self.assertRegex("+++", regex)
		self.assertRegex("---", regex)
		self.assertRegex("++--", regex)
	# async def test_getMessageRegex(self)

	async def test__buildVoteMessage(self):
		pEvaluatorKarma = EvaluatorKarma()
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(0, 0), 'kem1W')
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(1, 0), '++')
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(0, 1), '--')
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(2, 0), '++ (x2)')
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(0, 2), '-- (x2)')
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(1, 1), '++ (x1), -- (x1)')
		self.assertEqual(pEvaluatorKarma._buildVoteMessage(6, 9), '++ (x6), -- (x9)')
	# async def test__buildVoteMessage(self)

	async def test__countMinusVotes(self):
		pEvaluatorKarma = EvaluatorKarma()
		self.assertEqual(pEvaluatorKarma._countMinusVotes(''), 0)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('-'), 0)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('--'), 1)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('---'), 1)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('----'), 1)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('-----'), 1)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('-- --'), 2)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('+--'), 1)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('abc--'), 1)
		self.assertEqual(pEvaluatorKarma._countMinusVotes('abc--+--'), 2)
	# async def test__countMinusVotes(self)

	async def test__countPlusVotes(self):
		pEvaluatorKarma = EvaluatorKarma()
		self.assertEqual(pEvaluatorKarma._countPlusVotes(''), 0)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('+'), 0)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('++'), 1)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('+++'), 1)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('++++'), 1)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('+++++'), 1)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('++ ++'), 2)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('-++'), 1)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('abc++'), 1)
		self.assertEqual(pEvaluatorKarma._countPlusVotes('abc++-++'), 2)
	# async def test__countPlusVotes(self)

	async def test_execute(self):
		pLocalVariables = LocalVariables()
		pLocalVariables.get = mock.Mock(return_value=70)
		pLocalVariables.write = mock.Mock()

		pEvaluatorKarma = EvaluatorKarma()
		pEvaluatorKarma.pLocalVariables = pLocalVariables

		pChannel = MessageChannel(name='unittest')
		pMessage = Message(channel=pChannel, content='--')

		message = await pEvaluatorKarma.execute(pMessage)
		self.assertEqual(message, "Successfully voted --, current streamer karma: 69")

		pLocalVariables.get.assert_called_once_with('karma', 'unittest', 0)
		pLocalVariables.write.assert_called_once_with('karma', 'unittest', 69)
	# async def test_execute(self)
# class TestEvaluatorKarma(unittest.IsolatedAsyncioTestCase)