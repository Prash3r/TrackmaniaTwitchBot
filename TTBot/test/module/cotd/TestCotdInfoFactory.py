# pylib
import datetime
import unittest

# local
from TTBot.module.cotd.CotdInfo import CotdInfo
from TTBot.module.cotd.CotdInfoFactory import CotdInfoFactory

class TestCotdInfoFactory(unittest.TestCase):
	def test_createFromCacheQuery_Mysql(self):
		pDateStart = datetime.datetime(year=2022, month=1, day=25, hour=23, minute=1, second=4)
		pDateEnd = datetime.datetime(year=2022, month=1, day=25, hour=23, minute=1, second=26)

		dataInfo = {
			'id': 1234,
			'name': 'unittest #1234',
			'num_players': 69,
			'date_start': pDateStart,
			'date_end': pDateEnd,
			'winner': 'unittest'
		}

		pCotdInfoFactory = CotdInfoFactory()
		pCotdInfo = pCotdInfoFactory.createFromCacheQuery(dataInfo)
		self.assertEqual(pCotdInfo.getId(), 1234)
		self.assertEqual(pCotdInfo.getName(), 'unittest #1234')
		self.assertEqual(pCotdInfo.getNumPlayers(), 69)
		self.assertEqual(pCotdInfo.getDateStart(), pDateStart)
		self.assertEqual(pCotdInfo.getDateEnd(), pDateEnd)
		self.assertEqual(pCotdInfo.getWinner(), 'unittest')
	# def test_createFromCacheQuery_Mysql(self)

	def test_createFromCacheQuery_Sqlite(self):
		pDateStart = datetime.datetime(year=2022, month=1, day=25, hour=23, minute=1, second=4)
		pDateEnd = datetime.datetime(year=2022, month=1, day=25, hour=23, minute=1, second=26)

		dataInfo = {
			'id': 1234,
			'name': 'unittest #1234',
			'num_players': 69,
			'date_start': '2022-01-25 23:01:04',
			'date_end': '2022-01-25 23:01:26',
			'winner': 'unittest'
		}

		pCotdInfoFactory = CotdInfoFactory()
		pCotdInfo = pCotdInfoFactory.createFromCacheQuery(dataInfo)
		self.assertEqual(pCotdInfo.getId(), 1234)
		self.assertEqual(pCotdInfo.getName(), 'unittest #1234')
		self.assertEqual(pCotdInfo.getNumPlayers(), 69)
		self.assertEqual(pCotdInfo.getDateStart(), pDateStart)
		self.assertEqual(pCotdInfo.getDateEnd(), pDateEnd)
		self.assertEqual(pCotdInfo.getWinner(), 'unittest')
	# def test_createFromCacheQuery_Sqlite(self)

	def test_createFromTrackmaniaIo(self):
		dataInfo = {
			'id': 1234,
			'name': 'unittest #1234',
			'players': 69,
			'starttime': 1234567890,
			'endtime': 9876543210
		}

		pDateStart = datetime.datetime(year=2009, month=2, day=13, hour=23, minute=31, second=30)
		pDateEnd = datetime.datetime(year=2282, month=12, day=22, hour=20, minute=13, second=30)

		pCotdInfoFactory = CotdInfoFactory()
		pCotdInfo = pCotdInfoFactory.createFromTrackmaniaIo(dataInfo, 'unittest')
		self.assertEqual(pCotdInfo.getId(), 1234)
		self.assertEqual(pCotdInfo.getName(), 'unittest #1234')
		self.assertEqual(pCotdInfo.getNumPlayers(), 69)
		self.assertEqual(pCotdInfo.getDateStart(), pDateStart)
		self.assertEqual(pCotdInfo.getDateEnd(), pDateEnd)
		self.assertEqual(pCotdInfo.getWinner(), 'unittest')
	# def test_createFromTrackmaniaIo(self)

	def test_createNext(self):
		pNow = datetime.datetime.now()
		pDistance = datetime.timedelta(hours=4)
		pDuration = datetime.timedelta(hours=1)
		pMarginOfError = datetime.timedelta(hours=1)

		pCotdInfoPrev = CotdInfo()
		pCotdInfoPrev.setDateStart(pNow - pDistance)
		pCotdInfoPrev.setDateEnd(pNow - pDistance + pDuration)

		pCotdInfoFactory = CotdInfoFactory()
		pCotdInfoNext = pCotdInfoFactory.createNext(pCotdInfoPrev)

		self.assertEqual(pCotdInfoNext.getId(), -1)
		self.assertEqual(pCotdInfoNext.getName(), '')
		self.assertEqual(pCotdInfoNext.getNumPlayers(), 0)
		self.assertGreaterEqual(pCotdInfoNext.getDateStart(), pNow + pDistance - pMarginOfError)
		self.assertGreaterEqual(pCotdInfoNext.getDateEnd(), pNow + pDistance + pDuration - pMarginOfError)
		self.assertIsNone(pCotdInfoNext.getWinner())
	# def test_createNext(self)
# class TestCotdInfoFactory(unittest.TestCase)