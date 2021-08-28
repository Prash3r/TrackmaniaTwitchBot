# pylib
import unittest
from unittest import mock

# local
from TTBot.logic.ModuleFactory import ModuleFactory
from TTBot.optional.commands.Command import Command
from TTBot.optional.commands.CommandList import CommandList
from TTBot.optional.commands.CommandMm import CommandMm
from TTBot.optional.evaluators.Evaluator import Evaluator
from TTBot.optional.evaluators.EvaluatorList import EvaluatorList
from TTBot.optional.evaluators.EvaluatorPing import EvaluatorPing
from TTBot.optional.Module import Module

class TestModuleFactory(unittest.TestCase):
	def test_createCommand(self):
		pModuleFactory = ModuleFactory()
		pModuleFactory._create = mock.Mock(return_value=CommandMm())

		pCommandMm = pModuleFactory.createCommand(CommandMm)
		self.assertIsInstance(pCommandMm, CommandMm)

		pCommandList = CommandList()
		commandClasses = pCommandList.getAllCommandClasses()

		for commandClass in commandClasses:
			pModuleFactory._create = mock.Mock(return_value=commandClass())
			pCommand = pModuleFactory.createCommand(commandClass)
			self.assertIsInstance(pCommand, Module)
			self.assertIsInstance(pCommand, Command)
		# for commandClass in commandClasses
	# def test_createCommand(self)

	def test_createEvaluator(self):
		pModuleFactory = ModuleFactory()
		pModuleFactory._create = mock.Mock(return_value=EvaluatorPing())

		pEvaluatorPing = pModuleFactory.createEvaluator(EvaluatorPing)
		self.assertIsInstance(pEvaluatorPing, EvaluatorPing)

		pEvaluatorList = EvaluatorList()
		evaluatorClasses = pEvaluatorList.getAllEvaluatorClasses()

		for evaluatorClass in evaluatorClasses:
			pModuleFactory._create = mock.Mock(return_value=evaluatorClass())
			pEvaluator = pModuleFactory.createEvaluator(evaluatorClass)
			self.assertIsInstance(pEvaluator, Module)
			self.assertIsInstance(pEvaluator, Evaluator)
		# for evaluatorClass in evaluatorClasses
	# def test_createEvaluator(self)
# class TestModuleFactory(unittest.TestCase)