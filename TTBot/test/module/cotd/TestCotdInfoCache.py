# pylib
import datetime

# vendor
import minidi

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.module.cotd.CotdInfo import CotdInfo
from TTBot.module.cotd.CotdInfoCache import CotdInfoCache
from TTBot.module.cotd.CotdInfoFactory import CotdInfoFactory
from TTBot.test.DbIntegrationTest import DbIntegrationTest

class TestCotdInfoCache(DbIntegrationTest):
	pCotdInfoCache: CotdInfoCache

	def setUp(self):
		super().setUpBeforeEach('cotd_info_cache.sqlite')

		pCotdInfoFactory: CotdInfoFactory = minidi.get(CotdInfoFactory)
		pDbConnector: DbConnector = minidi.get(DbConnector)

		pNow = datetime.datetime.now()
		pDuration = datetime.timedelta(hours=1)
		pDistance = datetime.timedelta(hours=4)

		pCotdInfoPrevPrev = CotdInfo()
		pCotdInfoPrevPrev.setId(1233)
		pCotdInfoPrevPrev.setName('CotD #1233')
		pCotdInfoPrevPrev.setNumPlayers(69)
		pCotdInfoPrevPrev.setDateStart(pNow - 2*pDistance)
		pCotdInfoPrevPrev.setDateEnd(pNow - 2*pDistance + pDuration)
		pCotdInfoPrevPrev.setWinner('unittest')

		pCotdInfoPrev = CotdInfo()
		pCotdInfoPrev.setId(1234)
		pCotdInfoPrev.setName('CotD #1234')
		pCotdInfoPrev.setNumPlayers(2468)
		pCotdInfoPrev.setDateStart(pNow - pDistance)
		pCotdInfoPrev.setDateEnd(pNow - pDistance + pDuration)
		pCotdInfoPrev.setWinner('unittest')

		pCotdInfoNext = CotdInfo()
		pCotdInfoNext.setId(1235)
		pCotdInfoNext.setName('CotD #1235')
		pCotdInfoNext.setDateStart(pNow + pDistance)
		pCotdInfoNext.setDateEnd(pNow + pDistance + pDuration)

		self.pCotdInfoCache = CotdInfoCache()
		self.pCotdInfoCache.pCotdInfoFactory = pCotdInfoFactory
		self.pCotdInfoCache.pDbConnector = pDbConnector
		self.pCotdInfoCache.afterInit()
		self.pCotdInfoCache.write(pCotdInfoPrevPrev)
		self.pCotdInfoCache.write(pCotdInfoPrev)
		self.pCotdInfoCache.write(pCotdInfoNext)
	# def setUp(self)

	def tearDown(self):
		super().tearDownAfterEach('cotd_info_cache.sqlite')
	# def tearDown(self)
	
	def test_afterInit(self):
		pDbConnector = self.pCotdInfoCache.pDbConnector
		rows: list = pDbConnector.fetch("SELECT * FROM `cotd_info`;")
		self.assertEqual(len(rows), 3)

		for row in rows:
			row: dict
			self.assertIn('id', row.keys())
			self.assertIn('name', row.keys())
			self.assertIn('num_players', row.keys())
			self.assertIn('date_start', row.keys())
			self.assertIn('date_end', row.keys())
			self.assertIn('winner', row.keys())
		# for row in rows
	# def test_afterInit(self)

	def test_getIdsWithWinner(self):
		idsWithWinner = self.pCotdInfoCache.getIdsWithWinner(0)
		self.assertListEqual(idsWithWinner, [])

		idsWithWinner = self.pCotdInfoCache.getIdsWithWinner(1)
		self.assertListEqual(idsWithWinner, [1234])

		idsWithWinner = self.pCotdInfoCache.getIdsWithWinner(2)
		self.assertListEqual(idsWithWinner, [1234, 1233])

		idsWithWinner = self.pCotdInfoCache.getIdsWithWinner(3)
		self.assertListEqual(idsWithWinner, [1234, 1233])
	# def test_getIdsWithWinner(self)

	def test_getNext(self):
		pNow = datetime.datetime.now()
		pCotdInfoNext = self.pCotdInfoCache.getNext()

		self.assertEqual(pCotdInfoNext.getId(), 1235)
		self.assertEqual(pCotdInfoNext.getName(), 'CotD #1235')
		self.assertEqual(pCotdInfoNext.getNumPlayers(), 0)
		self.assertGreater(pCotdInfoNext.getDateStart(), pNow)
		self.assertGreater(pCotdInfoNext.getDateEnd(), pNow)
		self.assertIsNone(pCotdInfoNext.getWinner())
	# def test_getNext(self)

	def test_getPrev(self):
		pNow = datetime.datetime.now()
		pCotdInfoNext = self.pCotdInfoCache.getPrev()

		self.assertEqual(pCotdInfoNext.getId(), 1234)
		self.assertEqual(pCotdInfoNext.getName(), 'CotD #1234')
		self.assertEqual(pCotdInfoNext.getNumPlayers(), 2468)
		self.assertLess(pCotdInfoNext.getDateStart(), pNow)
		self.assertLess(pCotdInfoNext.getDateEnd(), pNow)
		self.assertEqual(pCotdInfoNext.getWinner(), 'unittest')
	# def test_getPrev(self)

	def test_write(self):
		pNow = datetime.datetime.now()
		pCotdInfo = CotdInfo()
		pCotdInfo.setId(1337)
		pCotdInfo.setName('test_write')
		pCotdInfo.setNumPlayers(42)
		pCotdInfo.setDateStart(pNow)
		pCotdInfo.setDateEnd(pNow + datetime.timedelta(hours=1))
		pCotdInfo.setWinner('test_write')

		success = self.pCotdInfoCache.write(pCotdInfo)
		self.assertTrue(success)

		pDbConnector = self.pCotdInfoCache.pDbConnector
		rows: list = pDbConnector.fetch("SELECT * FROM `cotd_info` WHERE `id` = 1337;")
		self.assertEqual(len(rows), 1)
		
		row: dict = rows[0]
		self.assertEqual(len(row), 6)

		self.assertIn('id', row.keys())
		self.assertIn('name', row.keys())
		self.assertIn('num_players', row.keys())
		self.assertIn('date_start', row.keys())
		self.assertIn('date_end', row.keys())
		self.assertIn('winner', row.keys())

		self.assertEqual(row['id'], 1337)
		self.assertEqual(row['name'], 'test_write')
		self.assertEqual(row['num_players'], 42)
		self.assertEqual(row['winner'], 'test_write')
	# def test_write(self)
# class TestCotdInfoCache(unittest.TestCase)