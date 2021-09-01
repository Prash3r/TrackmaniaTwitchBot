# pylib
import unittest

# local
from TTBot.module.ping.EvaluatorPing import EvaluatorPing

class TestEvaluatorPing(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		pEvaluatorPing = EvaluatorPing()
		regex = pEvaluatorPing.getMessageRegex()
		self.assertRegex('ping', regex)
		self.assertRegex('hey ping ping', regex)
		self.assertNotRegex('pnig', regex)
	# async def test_getMessageRegex(self)

	async def test_execute(self):
		pEvaluatorPing = EvaluatorPing()
		result = await pEvaluatorPing.execute(object())
		self.assertEqual(result, 'pong')
	# async def test_execute(self)
# class TestEvaluatorPing(unittest.IsolatedAsyncioTestCase)