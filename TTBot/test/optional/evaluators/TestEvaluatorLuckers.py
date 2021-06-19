# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.ProcessVariables import ProcessVariables
from TTBot.optional.evaluators.EvaluatorLuckers import EvaluatorLuckers

class TestEvaluatorLuckers(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		regex = EvaluatorLuckers.getMessageRegex()
		self.assertRegex('luckers', regex)
		self.assertRegex('hey luckers', regex)
		self.assertRegex('luckers, you KEKEGA', regex)
		self.assertNotRegex('lucky', regex)
	# async def test_getMessageRegex(self)

	async def test_execute(self):
		pProcessVariables = ProcessVariables()
		pProcessVariables.get = mock.Mock(return_value=3)
		pProcessVariables.write = mock.Mock()

		pEvaluatorLuckers = EvaluatorLuckers()
		pEvaluatorLuckers.pProcessVariables = pProcessVariables
		pEvaluatorLuckers.messageAuthor = 'unittest'

		result = await pEvaluatorLuckers.execute()
		self.assertEqual(result, "Turbo was called Luckers for 4 times ... please just dont, @unittest!")

		pEvaluatorLuckers.pProcessVariables.get.assert_called_once_with('luckerscounter', 0)
		pEvaluatorLuckers.pProcessVariables.write.assert_called_once_with('luckerscounter', 4)
	# async def test_execute(self)
# class TestEvaluatorLuckers(EvaluatorLuckers)