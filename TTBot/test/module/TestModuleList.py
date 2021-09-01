# pylib
import unittest

# local
from TTBot.module.Command import Command
from TTBot.module.Evaluator import Evaluator
from TTBot.module.Module import Module
from TTBot.module.ModuleList import ModuleList

class TestModuleList(unittest.TestCase):
	def test_getCommandClasses(self):
		pModuleList = ModuleList()
		commandClasses = pModuleList.getCommandClasses()
		for commandClass in commandClasses:
			pCommand = commandClass()
			self.assertIsInstance(pCommand, Command)
		# for commandClass in commandClasses
	# def test_getCommandClasses(self)

	def test_getEvaluatorClasses(self):
		pModuleList = ModuleList()
		evaluatorClasses = pModuleList.getEvaluatorClasses()

		for evaluatorClass in evaluatorClasses:
			pEvaluator = evaluatorClass()
			self.assertIsInstance(pEvaluator, Evaluator)
		# for evaluatorClass in evaluatorClasses
	# def test_getEvaluatorClasses(self)

	def test_getModuleClasses(self):
		pModuleList = ModuleList()
		moduleClasses = pModuleList.getEvaluatorClasses()

		for moduleClass in moduleClasses:
			pModule = moduleClass()
			self.assertIsInstance(pModule, Module)
		# for moduleClass in moduleClasses
	# def test_getModuleClasses(self)

	def test_getModuleIds(self):
		pModuleList = ModuleList()
		moduleIds = pModuleList.getModuleIds()

		for moduleId in moduleIds:
			self.assertEqual(moduleIds.count(moduleId), 1)
	# def test_getModuleIds(self)
# class TestModuleList(unittest.TestCase)