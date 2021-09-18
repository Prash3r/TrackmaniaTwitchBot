# vendor
import minidi

# local
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.DbConnector import DbConnector
from TTBot.test.DbIntegrationTest import DbIntegrationTest

class TestDbConnector(DbIntegrationTest):
	pDbConnector: DbConnector

	def setUp(self):
		super().setUpBeforeEach('db_connector.sqlite')

		pDbConnection: DbConnection = minidi.get(DbConnection)
		pDbConnection.query("CREATE TABLE `test_db_connector` ( \
			`integer` INT(11), \
			`string` VARCHAR(32) \
		);")
		pDbConnection.query("INSERT INTO `test_db_connector` (`integer`, `string`) \
			VALUES (42, 'answer'), (69, 'nice');")
		
		self.pDbConnector = DbConnector()
		self.pDbConnector.pDbConnection = pDbConnection
	# def setUp(self)

	def tearDown(self):
		super().tearDownAfterEach('db_connector.sqlite')
	# def tearDown(self)

	def test_execute(self):
		rowcount = self.pDbConnector.execute(
			"UPDATE `test_db_connector` SET `string` = ? WHERE `integer` = ?;",
			['universe', 42]
		)

		self.assertEqual(rowcount, 1)
	# def test_execute(self)

	def test_fetch(self):
		rows = self.pDbConnector.fetch("SELECT * FROM `test_db_connector`;")
		self.assertEqual(len(rows), 2)
		
		rowAnswer: dict = rows[0]
		self.assertEqual(len(rowAnswer), 2)
		self.assertIn('integer', rowAnswer.keys())
		self.assertIn('string', rowAnswer.keys())
		self.assertEqual(rowAnswer['integer'], 42)
		self.assertEqual(rowAnswer['string'], 'answer')
		
		rowNice: dict = rows[1]
		self.assertEqual(len(rowNice), 2)
		self.assertIn('integer', rowNice.keys())
		self.assertIn('string', rowNice.keys())
		self.assertEqual(rowNice['integer'], 69)
		self.assertEqual(rowNice['string'], 'nice')
	# def test_fetch(self)

	def test_getColumns(self):
		columns = self.pDbConnector.getColumns('test_db_connector')
		self.assertListEqual(columns, ['integer', 'string'])
	# def test_getColumns(self)
# class TestDbConnector(DbIntegrationTest)