# pylib
import unittest
from unittest import mock

# local
from TTBot.optional.evaluators.EvaluatorLuckers import EvaluatorLuckers

class TestEvaluatorLuckers(unittest.IsolatedAsyncioTestCase):
	async def test_execute(self):
		pEvaluatorLuckers = EvaluatorLuckers()
		pEvaluatorLuckers.funcGetPV = mock.Mock(return_value=3)
		pEvaluatorLuckers.funcWritePV = mock.Mock()
		pEvaluatorLuckers.messageAuthor = 'unittest'

		result = await pEvaluatorLuckers.execute()
		self.assertEqual(result, "Turbo was called Luckers for 4 times ... please just dont, @unittest!")

		pEvaluatorLuckers.funcGetPV.assert_called_once_with('luckerscounter')
		pEvaluatorLuckers.funcWritePV.assert_called_once_with('luckerscounter', 4, 3)
	# async def test_execute(self)
# class TestEvaluatorLuckers(EvaluatorLuckers)