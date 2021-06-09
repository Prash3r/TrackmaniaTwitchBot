# pylib
import unittest

# local
from TTBot.optional.evaluators.Evaluator import Evaluator
from TTBot.optional.evaluators.EvaluatorFactory import EvaluatorFactory
from TTBot.optional.evaluators.EvaluatorLuckers import EvaluatorLuckers
from TTBot.optional.evaluators.EvaluatorOoga import EvaluatorOoga
from TTBot.optional.evaluators.EvaluatorPing import EvaluatorPing

class DynamicObject:
	pass

class TestEvaluatorFactory(unittest.TestCase):
	def test_create_default(self):
		ctx = DynamicObject()
		ctx.author = DynamicObject()
		ctx.author.name = 'unittest'
		ctx.content = 'this is a unittest text artificially triggering for every evaluator'
		ctx.channel = DynamicObject()
		ctx.channel.name = 'unittestchannel'

		pEvaluatorInstance = EvaluatorFactory.create(EvaluatorOoga, None, ctx)
		self.assertIsInstance(pEvaluatorInstance, Evaluator)
		self.assertIsInstance(pEvaluatorInstance, EvaluatorOoga)
	# def test_create_default(self)

	def test_create_luckers(self):
		pTwitchBot = DynamicObject()
		pTwitchBot.DB_GetPV = lambda: 'database read query'
		pTwitchBot.DB_WritePV = lambda: 'database write query'
		
		ctx = DynamicObject()
		ctx.author = DynamicObject()
		ctx.author.name = 'unittest'
		ctx.content = 'this is a text containing the word luckers and others'
		ctx.channel = DynamicObject()
		ctx.channel.name = 'unittestchannel'

		pEvaluatorInstance = EvaluatorFactory.create(EvaluatorLuckers, pTwitchBot, ctx)
		self.assertIsInstance(pEvaluatorInstance, Evaluator)
		self.assertIsInstance(pEvaluatorInstance, EvaluatorLuckers)
		self.assertEqual(pEvaluatorInstance.funcGetPV(), 'database read query')
		self.assertEqual(pEvaluatorInstance.funcWritePV(), 'database write query')
		self.assertEqual(pEvaluatorInstance.messageAuthor, 'unittest')
	# def test_create_luckers(self):
# class TestEvaluatorFactory(unittest.TestCase)