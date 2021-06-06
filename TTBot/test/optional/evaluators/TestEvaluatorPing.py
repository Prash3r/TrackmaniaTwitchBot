# pylib
import unittest

# local
from TTBot.optional.evaluators.EvaluatorPing import EvaluatorPing

class TestEvaluatorPing(unittest.IsolatedAsyncioTestCase):
	async def test_execute(self):
		pEvaluatorPing = EvaluatorPing()
		result = await pEvaluatorPing.execute()
		self.assertEqual(result, 'pong')
	# async def test_execute(self)
# class TestEvaluatorPing(unittest.IsolatedAsyncioTestCase)