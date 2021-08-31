# pylib
import datetime
import unittest

# local
from TTBot.module.matchmaking.MatchmakingData import MatchmakingData

class TestMatchmakingData(unittest.TestCase):
	def test_player(self):
		pMatchmakingData = MatchmakingData()
		self.assertEqual(pMatchmakingData.getPlayer(), '')

		pMatchmakingData.setPlayer('player')
		self.assertEqual(pMatchmakingData.getPlayer(), 'player')
	# def test_player(self)

	def test_playerAccountId(self):
		pMatchmakingData = MatchmakingData()
		self.assertEqual(pMatchmakingData.getPlayerAccountId(), '')

		pMatchmakingData.setPlayerAccountId('12345')
		self.assertEqual(pMatchmakingData.getPlayerAccountId(), '12345')
	# def test_playerAccountId(self)

	def test_rank(self):
		pMatchmakingData = MatchmakingData()
		self.assertEqual(pMatchmakingData.getRank(), 0)

		pMatchmakingData.setRank(46)
		self.assertEqual(pMatchmakingData.getRank(), 46)
	# def test_rank(self)

	def test_score(self):
		pMatchmakingData = MatchmakingData()
		self.assertEqual(pMatchmakingData.getScore(), 0)

		pMatchmakingData.setScore(1234)
		self.assertEqual(pMatchmakingData.getScore(), 1234)
	# def test_score(self)

	def test_timestamp(self):
		pMatchmakingData = MatchmakingData()
		self.assertEqual(pMatchmakingData.getTimestamp(), None)

		pNow = datetime.datetime.now()
		pMatchmakingData.setTimestamp(pNow)
		self.assertEqual(pMatchmakingData.getTimestamp(), pNow)
	# def test_timestamp(self)
# class TestMatchmakingData(unittest.TestCase)