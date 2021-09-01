# pylib
import unittest
from unittest import mock

# local
from TTBot.optional.commands.CommandList import CommandList
from TTBot.module.roll.CommandRoll import CommandRoll
from TTBot.module.score.CommandScore import CommandScore
from TTBot.optional.evaluators.EvaluatorList import EvaluatorList
from TTBot.module.ooga.EvaluatorOoga import EvaluatorOoga
from TTBot.optional.evaluators.EvaluatorPing import EvaluatorPing
from TTBot.optional.ModuleList import ModuleList

class TestModuleList(unittest.TestCase):
	def test_getAllModuleClasses(self):
		pCommandList = CommandList()
		pCommandList.getAllCommandClasses = mock.Mock(return_value=[CommandRoll, CommandScore])

		pEvaluatorList = EvaluatorList()
		pEvaluatorList.getAllEvaluatorClasses = mock.Mock(return_value=[EvaluatorOoga, EvaluatorPing])

		pModuleList = ModuleList()
		pModuleList.pCommandList = pCommandList
		pModuleList.pEvaluatorList = pEvaluatorList

		expected = [CommandRoll, CommandScore, EvaluatorOoga, EvaluatorPing]
		self.assertListEqual(pModuleList.getAllModuleClasses(), expected)

		pCommandList.getAllCommandClasses.assert_called_once()
		pEvaluatorList.getAllEvaluatorClasses.assert_called_once()
	# def test_getAllModuleClasses(self)

	def test_getAllModuleIds(self):
		pCommandList = CommandList()
		pCommandList.getAllCommandClasses = mock.Mock(return_value=[CommandRoll, CommandScore])

		pEvaluatorList = EvaluatorList()
		pEvaluatorList.getAllEvaluatorClasses = mock.Mock(return_value=[EvaluatorOoga, EvaluatorPing])

		pModuleList = ModuleList()
		pModuleList.pCommandList = pCommandList
		pModuleList.pEvaluatorList = pEvaluatorList

		expected = ['roll', 'score', 'ooga', 'ping']
		self.assertListEqual(pModuleList.getAllModuleIds(), expected)

		pCommandList.getAllCommandClasses.assert_called_once()
		pEvaluatorList.getAllEvaluatorClasses.assert_called_once()
	# def test_getAllModuleIds(self)
# class TestModuleList(unittest.TestCase)