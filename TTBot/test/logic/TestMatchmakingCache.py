# pylib
import datetime
import unittest
from unittest import mock

# local
from TTBot.logic.DateTimeChecker import DateTimeChecker
from TTBot.logic.MatchmakingCache import MatchmakingCache
from TTBot.logic.MatchmakingDataFactory import MatchmakingDataFactory

class TestMatchmakingCache(unittest.TestCase):
	def test_get(self):
		pTimestampNow = datetime.datetime.now()
		pTimestampSeventyMinutes = pTimestampNow - datetime.timedelta(minutes=70)
		pTimestampTwoDays        = pTimestampNow - datetime.timedelta(days=2)

		rows = [
			[10, 'fetch_new', pTimestampTwoDays, 3947],
			[42, 'use_cache', pTimestampNow, 3652],
			[68, 'fetch_new', pTimestampSeventyMinutes, 3574],
			[69, 'use_cache', pTimestampSeventyMinutes, 3572],
			[70, 'fetch_new', pTimestampSeventyMinutes, 3569],
		]

		pMariaDbWrapper = mock.Mock()
		pMariaDbWrapper.fetch = mock.Mock(return_value=rows)

		pMatchmakingCache = MatchmakingCache()
		pMatchmakingCache.pDateTimeChecker = DateTimeChecker()
		pMatchmakingCache.pMariaDbWrapper = pMariaDbWrapper
		pMatchmakingCache.pMatchmakingDataFactory = MatchmakingDataFactory()

		cachedData = pMatchmakingCache.get('playerLoginPart')
		pMariaDbWrapper.fetch.assert_called_once_with("SELECT ranks_rank, ranks_displayname, ts, ranks_score FROM mmranking WHERE ranks_displayname = 'playerLoginPart';")

		for pMatchmakingData in cachedData:
			self.assertIn(pMatchmakingData.getRank(), [42, 69])
			self.assertEqual(pMatchmakingData.getPlayer(), 'use_cache')
		# for pMatchmakingData in cachedData
	# def test_get(self)
# class TestMatchmakingCache(unittest.TestCase)