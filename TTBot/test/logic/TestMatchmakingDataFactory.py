# pylib
import datetime
import unittest

# local
from TTBot.logic.MatchmakingDataFactory import MatchmakingDataFactory

class TestMatchmakingDataFactory(unittest.TestCase):
	def test_createFromCacheQuery(self):
		pMatchmakingDataFactory = MatchmakingDataFactory()
		pTimestamp = datetime.datetime.now()
		cacheData = {
			'ranks_rank': 42,
			'ranks_displayname': 'playername',
			'ts': pTimestamp,
			'ranks_score': 1234
		}

		pMatchmakingData = pMatchmakingDataFactory.createFromCacheQuery(cacheData)
		self.assertEqual(pMatchmakingData.getPlayer(), 'playername')
		self.assertEqual(pMatchmakingData.getRank(), 42)
		self.assertEqual(pMatchmakingData.getScore(), 1234)
		self.assertEqual(pMatchmakingData.getTimestamp(), pTimestamp)
	# def test_createFromCacheQuery(self)

	def test_createFromTrackmaniaIO(self):
		pMatchmakingDataFactory = MatchmakingDataFactory()
		tmIoData = {
			'player': {'name': 'playername'},
			'matchmaking': [
				{
					'rank': 42,
					'score': 1234,
					'accountid': 'FACADE01'
				}
			]
		}

		pMatchmakingData = pMatchmakingDataFactory.createFromTrackmaniaIO(tmIoData)
		self.assertEqual(pMatchmakingData.getPlayer(), 'playername')
		self.assertEqual(pMatchmakingData.getPlayerAccountId(), 'FACADE01')
		self.assertEqual(pMatchmakingData.getRank(), 42)
		self.assertEqual(pMatchmakingData.getScore(), 1234)
	# def test_createFromTrackmaniaIO(self)
# class TestMatchmakingDataFactory(unittest.TestCase)