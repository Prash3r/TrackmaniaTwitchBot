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
			{'ranks_rank': 10, 'ranks_displayname': 'fetch_new', 'ts': pTimestampTwoDays       , 'ranks_score': 3947},
			{'ranks_rank': 42, 'ranks_displayname': 'use_cache', 'ts': pTimestampNow           , 'ranks_score': 3652},
			{'ranks_rank': 68, 'ranks_displayname': 'fetch_new', 'ts': pTimestampSeventyMinutes, 'ranks_score': 3574},
			{'ranks_rank': 69, 'ranks_displayname': 'use_cache', 'ts': pTimestampSeventyMinutes, 'ranks_score': 3572},
			{'ranks_rank': 70, 'ranks_displayname': 'fetch_new', 'ts': pTimestampSeventyMinutes, 'ranks_score': 3569}
		]

		pDbConnector = mock.Mock()
		pDbConnector.fetch = mock.Mock(return_value=rows)

		pMatchmakingCache = MatchmakingCache()
		pMatchmakingCache.pDateTimeChecker = DateTimeChecker()
		pMatchmakingCache.pDbConnector = pDbConnector
		pMatchmakingCache.pMatchmakingDataFactory = MatchmakingDataFactory()

		cachedData = pMatchmakingCache.get('playerLoginPart')
		pDbConnector.fetch.assert_called_once_with("SELECT ranks_rank, ranks_displayname, ts, ranks_score FROM mmranking WHERE ranks_displayname = 'playerLoginPart';")

		for pMatchmakingData in cachedData:
			self.assertIn(pMatchmakingData.getRank(), [42, 69])
			self.assertEqual(pMatchmakingData.getPlayer(), 'use_cache')
		# for pMatchmakingData in cachedData
	# def test_get(self)
# class TestMatchmakingCache(unittest.TestCase)