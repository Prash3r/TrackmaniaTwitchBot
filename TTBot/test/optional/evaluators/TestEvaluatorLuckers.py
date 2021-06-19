# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.MariaDbWrapper import MariaDbWrapper
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
		pMariaDbWrapper = MariaDbWrapper()
		pMariaDbWrapper.getProcessVariable = mock.Mock(return_value=3)
		pMariaDbWrapper.writeProcessVariable = mock.Mock()

		pEvaluatorLuckers = EvaluatorLuckers()
		pEvaluatorLuckers.pMariaDbWrapper = pMariaDbWrapper
		pEvaluatorLuckers.messageAuthor = 'unittest'

		result = await pEvaluatorLuckers.execute()
		self.assertEqual(result, "Turbo was called Luckers for 4 times ... please just dont, @unittest!")

		pEvaluatorLuckers.pMariaDbWrapper.getProcessVariable.assert_called_once_with('luckerscounter')
		pEvaluatorLuckers.pMariaDbWrapper.writeProcessVariable.assert_called_once_with('luckerscounter', 4, 3)
	# async def test_execute(self)
# class TestEvaluatorLuckers(EvaluatorLuckers)