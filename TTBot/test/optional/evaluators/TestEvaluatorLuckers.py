# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.GlobalVariables import GlobalVariables
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.optional.evaluators.EvaluatorLuckers import EvaluatorLuckers

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

		pMessageEvaluator = MessageEvaluator()
		pMessageEvaluator.getAuthorName = mock.Mock(return_value='unittest')

		pEvaluatorLuckers = EvaluatorLuckers()
		pEvaluatorLuckers.pGlobalVariables = pGlobalVariables
		pEvaluatorLuckers.pMessageEvaluator = pMessageEvaluator

		pMessage = mock.Mock()
		result = await pEvaluatorLuckers.execute(pMessage)
		self.assertEqual(result, "Turbo was called Luckers for 4 times ... please just dont, @unittest!")

		pEvaluatorLuckers.pGlobalVariables.get.assert_called_once_with('luckerscounter', 0)
		pEvaluatorLuckers.pGlobalVariables.write.assert_called_once_with('luckerscounter', 4)
		pEvaluatorLuckers.pMessageEvaluator.getAuthorName.assert_called_once_with(pMessage)
	# async def test_execute(self)
# class TestEvaluatorLuckers(EvaluatorLuckers)