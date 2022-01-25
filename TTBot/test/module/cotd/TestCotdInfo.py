# pylib
import datetime
import unittest

# local
from TTBot.module.cotd.CotdInfo import CotdInfo

class TestCotdInfo(unittest.TestCase):
	def test_dateEnd(self):
		pCotdInfo = CotdInfo()
		self.assertIsNone(pCotdInfo.getDateEnd())

		pNow = datetime.datetime.now()
		pCotdInfo.setDateEnd(pNow)
		self.assertEqual(pCotdInfo.getDateEnd(), pNow)
	# def test_dateEnd(self)

	def test_dateStart(self):
		pCotdInfo = CotdInfo()
		self.assertIsNone(pCotdInfo.getDateStart())

		pNow = datetime.datetime.now()
		pCotdInfo.setDateStart(pNow)
		self.assertEqual(pCotdInfo.getDateStart(), pNow)
	# def test_dateStart(self)

	def test_id(self):
		pCotdInfo = CotdInfo()
		self.assertEqual(pCotdInfo.getId(), -1)

		pCotdInfo.setId(1234)
		self.assertEqual(pCotdInfo.getId(), 1234)
	# def test_id(self)

	def test_name(self):
		pCotdInfo = CotdInfo()
		self.assertEqual(pCotdInfo.getName(), '')

		pCotdInfo.setName('CotD #1234')
		self.assertEqual(pCotdInfo.getName(), 'CotD #1234')
	# def test_name(self)

	def test_numPlayers(self):
		pCotdInfo = CotdInfo()
		self.assertEqual(pCotdInfo.getNumPlayers(), 0)

		pCotdInfo.setNumPlayers(69)
		self.assertEqual(pCotdInfo.getNumPlayers(), 69)
	# def test_numPlayers(self)

	def test_winner(self):
		pCotdInfo = CotdInfo()
		self.assertIsNone(pCotdInfo.getWinner())

		pCotdInfo.setWinner('unittest')
		self.assertEqual(pCotdInfo.getWinner(), 'unittest')
	# def test_id(self)
# class TestCotdInfo(unittest.TestCase)