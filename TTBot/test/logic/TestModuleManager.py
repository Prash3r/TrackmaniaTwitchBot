# pylib
from unittest import mock

# vendor
import minidi

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.module.ModuleList import ModuleList
from TTBot.test.DbIntegrationTest import DbIntegrationTest

class TestModuleManager(DbIntegrationTest):
	calledDisableWith: list
	pModuleManager: ModuleManager

	def setUp(self):
		super().setUp()

		pDbConnector: DbConnector = minidi.get(DbConnector)

		pModuleCallbackRunner = ModuleCallbackRunner()
		pModuleCallbackRunner.onModuleDisable = mock.Mock()
		pModuleCallbackRunner.onModuleEnable = mock.Mock()
		self.calledDisableWith = []

		pModuleList = ModuleList()
		pModuleList.getModuleIds = mock.Mock(return_value=['karma', 'mm', 'score'])

		self.pModuleManager = ModuleManager()
		self.pModuleManager.pDbConnector = pDbConnector
		self.pModuleManager.pModuleCallbackRunner = pModuleCallbackRunner
		self.pModuleManager.pModuleList = pModuleList
		self.pModuleManager.afterInit()
		self.pModuleManager.addChannel('integration_test')
		self.pModuleManager.activateModule('integration_test', 'mm', 5)
		self.pModuleManager.activateModule('integration_test', 'score', 1)
	# def setUp(self)

	def tearDown(self):
		if self.calledDisableWith:
			for disabledWith in self.calledDisableWith:
				self.pModuleManager.pModuleCallbackRunner.onModuleDisable.assert_any_call(disabledWith)
		else:
			self.pModuleManager.pModuleCallbackRunner.onModuleDisable.assert_not_called()

		self.pModuleManager.pModuleCallbackRunner.onModuleEnable.assert_any_call('mm')
		self.pModuleManager.pModuleCallbackRunner.onModuleEnable.assert_any_call('score')
		self.pModuleManager.pModuleList.getModuleIds.assert_called_once()

		super().tearDown()
	# def tearDown(self)

	def test_afterInit(self):
		pDbConnector = self.pModuleManager.pDbConnector
		rows: list = pDbConnector.fetch("SELECT * FROM `modules` WHERE `channel` = 'integration_test';")
		self.assertEqual(len(rows), 1)

		row: dict = rows[0]
		self.assertEqual(len(row), 5)

		self.assertIn('channel', row.keys())
		self.assertIn('ts', row.keys())
		self.assertIn('karma', row.keys())
		self.assertIn('mm', row.keys())
		self.assertIn('score', row.keys())

		self.assertEqual(row['channel'], 'integration_test')
		self.assertEqual(row['karma'], 0)
		self.assertEqual(row['mm'], 5)
		self.assertEqual(row['score'], 1)
	# def test_afterInit(self)

	def test_activateModule(self):
		result = self.pModuleManager.activateModule('integration_test', 'karma', 1)
		self.assertTrue(result)

		pDbConnector = self.pModuleManager.pDbConnector
		rows: list = pDbConnector.fetch("SELECT `karma` FROM `modules` WHERE `channel` = 'integration_test';")
		self.assertEqual(len(rows), 1)

		row: dict = rows[0]
		self.assertEqual(len(row), 1)
		self.assertIn('karma', row.keys())
		self.assertEqual(row['karma'], 1)

		self.pModuleManager.pModuleCallbackRunner.onModuleEnable.assert_called_with('karma')
	# def test_activateModule(self)

	def test_addChannel(self):
		self.pModuleManager.addChannel('test_function')

		pDbConnector = self.pModuleManager.pDbConnector
		rows: list = pDbConnector.fetch("SELECT `channel` FROM `modules`;")

		for row in rows:
			row: dict
			self.assertEqual(len(row), 1)
			self.assertIn('channel', row.keys())
			self.assertIn(row['channel'], ['integration_test', 'test_function'])
		# for row in rows
	# def test_addChannel(self)

	def test_deactivateModule(self):
		result = self.pModuleManager.deactivateModule('integration_test', 'score')
		self.assertTrue(result)

		pDbConnector = self.pModuleManager.pDbConnector
		rows: list = pDbConnector.fetch("SELECT `score` FROM `modules` WHERE `channel` = 'integration_test';")
		self.assertEqual(len(rows), 1)

		row: dict = rows[0]
		self.assertEqual(len(row), 1)
		self.assertIn('score', row.keys())
		self.assertEqual(row['score'], 0)

		self.calledDisableWith.append('score')
	# def test_deactivateModule(self)

	def test_getChannels(self):
		channels = self.pModuleManager.getChannels()
		self.assertListEqual(channels, ['integration_test'])
	# def test_getChannels(self)

	def test_getMinimumAccessLevel(self):
		karmaAccessLevel = self.pModuleManager.getMinimumAccessLevel('integration_test', 'karma')
		self.assertEqual(karmaAccessLevel, 0)

		karmaAccessLevel = self.pModuleManager.getMinimumAccessLevel('integration_test', 'mm')
		self.assertEqual(karmaAccessLevel, 5)

		karmaAccessLevel = self.pModuleManager.getMinimumAccessLevel('integration_test', 'score')
		self.assertEqual(karmaAccessLevel, 1)
	# def test_getMinimumAccessLevel(self)

	def test_listModules(self):
		modules = self.pModuleManager.listModules()
		self.assertListEqual(modules, ['karma', 'mm', 'score'])
	# def test_listModules(self)

	def test_listModulesForChannel(self):
		modules = self.pModuleManager.listModulesForChannel('integration_test')
		self.assertDictEqual(modules, {'karma': 0, 'mm': 5, 'score': 1})
	# def test_listModules(self)

	def test_removeChannel(self):
		self.pModuleManager.removeChannel('integration_test')

		pDbConnector = self.pModuleManager.pDbConnector
		rows: list = pDbConnector.fetch("SELECT * FROM `modules`;")
		self.assertListEqual(rows, [])
	# def test_removeChannel(self)
# class TestModuleManager(DbIntegrationTest)