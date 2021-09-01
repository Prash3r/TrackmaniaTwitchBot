# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.module.luckers.EvaluatorLuckers import EvaluatorLuckers

class TestEvaluatorLuckers(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		pEvaluatorLuckers = EvaluatorLuckers()
		regex = pEvaluatorLuckers.getMessageRegex()
		self.assertRegex('luckers', regex)
		self.assertRegex('hey luckers', regex)
		self.assertRegex('luckers, you KEKEGA', regex)
		self.assertNotRegex('lucky', regex)
	# async def test_getMessageRegex(self)

	async def test_execute(self):
		pGlobalVariables = GlobalVariables()
		pGlobalVariables.get = mock.Mock(return_value=3)
		pGlobalVariables.write = mock.Mock()

		pEvaluatorLuckers = EvaluatorLuckers()
		pEvaluatorLuckers.pGlobalVariables = pGlobalVariables

		pMessage = Message(author=MessageAuthor(name='unittest'))
		result = await pEvaluatorLuckers.execute(pMessage)
		self.assertEqual(result, "Turbo was called Luckers for 4 times ... please just dont, @unittest!")

		pGlobalVariables.get.assert_called_once_with('luckerscounter', 0)
		pGlobalVariables.write.assert_called_once_with('luckerscounter', 4)
	# async def test_execute(self)
# class TestEvaluatorLuckers(EvaluatorLuckers)