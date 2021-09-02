# pylib
import unittest

# local
from TTBot.module.ooga.EvaluatorOoga import EvaluatorOoga

class TestEvaluatorOoga(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		pEvaluatorOoga = EvaluatorOoga()
		regex = pEvaluatorOoga.getMessageRegex()
		self.assertRegex('ooga', regex)
		self.assertRegex('hey ooga booga', regex)
		self.assertNotRegex('booga', regex)
		self.assertNotRegex('ogoa', regex)
	# async def test_getMessageRegex(self)

	async def test_execute(self):
		pEvaluatorOoga = EvaluatorOoga()
		result = await pEvaluatorOoga.execute(object())
		self.assertEqual(result, 'booga')
	# async def test_execute(self)
# class TestEvaluatorOoga(unittest.IsolatedAsyncioTestCase)