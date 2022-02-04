# pylib
import datetime
import unittest
from unittest.mock import Mock

# local
from TTBot.logic.DateTimeFormatter import DateTimeFormatter
from TTBot.module.cotd.CommandCotd import CommandCotd
from TTBot.module.cotd.CotdInfo import CotdInfo
from TTBot.module.cotd.CotdInfoCache import CotdInfoCache
from TTBot.module.cotd.CotdInfoFactory import CotdInfoFactory
from TTBot.module.cotd.TrackmaniaIoCotd import TrackmaniaIoCotd

class TestCommandCotd(unittest.TestCase):
	def test_getCommandTrigger(self):
		pCommandCotd = CommandCotd()
		self.assertEqual(pCommandCotd.getCommandTrigger(), 'cotd')
	# def test_getCommandTrigger(self)

	def test_getModuleId(self):
		pCommandCotd = CommandCotd()
		self.assertEqual(pCommandCotd.getModuleId(), 'cotd')
	# def test_getModuleId(self)

	def test__buildCotdInfoMessage_default(self):
		pNow = datetime.datetime.now()
		pDistance = datetime.timedelta(hours=4)
		pDuration = datetime.timedelta(hours=1)

		pCotdInfoPrev = CotdInfo()
		pCotdInfoPrev.setDateEnd(pNow - pDistance + pDuration)
		pCotdInfoPrev.setWinner('unittest')

		pCotdInfoNext = CotdInfo()
		pCotdInfoNext.setDateStart(pNow + pDistance)

		pCotdInfoCache = CotdInfoCache()
		pCotdInfoCache.getPrev = Mock(return_value=pCotdInfoPrev)
		pCotdInfoCache.getNext = Mock(return_value=pCotdInfoNext)

		pCotdInfoFactory = CotdInfoFactory()
		pCotdInfoFactory.createNext = Mock(return_value=pCotdInfoNext)
		
		pDateTimeFormatter = DateTimeFormatter()
		pDateTimeFormatter.formatIntervalShort = Mock(side_effect=['3h', '4h'])

		pTrackmaniaIoCotd = TrackmaniaIoCotd()
		pTrackmaniaIoCotd.loadInfo = Mock()

		pCommandCotd = CommandCotd()
		pCommandCotd.pCotdInfoCache = pCotdInfoCache
		pCommandCotd.pCotdInfoFactory = pCotdInfoFactory
		pCommandCotd.pDateTimeFormatter = pDateTimeFormatter
		pCommandCotd.pTrackmaniaIoCotd = pTrackmaniaIoCotd

		message = pCommandCotd._buildCotdInfoMessage()
		self.assertEqual(message, 'Last CotD finished 3h ago, winner: unittest // next CotD starts in ~4h')

		pCotdInfoCache.getPrev.assert_called_once_with()
		pCotdInfoCache.getNext.assert_called_once_with()
		pCotdInfoFactory.createNext.assert_not_called()
		pDateTimeFormatter.formatIntervalShort.assert_called()
		pTrackmaniaIoCotd.loadInfo.assert_called_once_with()
	# def test__buildCotdInfoMessage_default(self)

	def test__buildCotdInfoMessage_estimateNext(self):
		pNow = datetime.datetime.now()
		pDistance = datetime.timedelta(hours=4)
		pDuration = datetime.timedelta(hours=1)

		pCotdInfoPrev = CotdInfo()
		pCotdInfoPrev.setDateStart(pNow - pDistance)
		pCotdInfoPrev.setDateEnd(pNow - pDistance + pDuration)
		pCotdInfoPrev.setWinner('unittest')

		pCotdInfoNext = CotdInfo()
		pCotdInfoNext.setDateStart(pNow + pDistance)
		pCotdInfoNext.setDateEnd(pNow + pDistance + pDuration)
		pCotdInfoNext.setWinner('unittest')

		pCotdInfoCache = CotdInfoCache()
		pCotdInfoCache.getPrev = Mock(return_value=pCotdInfoPrev)
		pCotdInfoCache.getNext = Mock(return_value=None)

		pCotdInfoFactory = CotdInfoFactory()
		pCotdInfoFactory.createNext = Mock(return_value=pCotdInfoNext)
		
		pDateTimeFormatter = DateTimeFormatter()
		pDateTimeFormatter.formatIntervalShort = Mock(side_effect=['3h', '4h'])

		pTrackmaniaIoCotd = TrackmaniaIoCotd()
		pTrackmaniaIoCotd.loadInfo = Mock()

		pCommandCotd = CommandCotd()
		pCommandCotd.pCotdInfoCache = pCotdInfoCache
		pCommandCotd.pCotdInfoFactory = pCotdInfoFactory
		pCommandCotd.pDateTimeFormatter = pDateTimeFormatter
		pCommandCotd.pTrackmaniaIoCotd = pTrackmaniaIoCotd

		message = pCommandCotd._buildCotdInfoMessage()
		self.assertEqual(message, 'Last CotD finished 3h ago, winner: unittest // next CotD starts in ~4h')

		pCotdInfoCache.getPrev.assert_called_once_with()
		pCotdInfoCache.getNext.assert_called_once_with()
		pCotdInfoFactory.createNext.assert_called_once_with(pCotdInfoPrev)
		pDateTimeFormatter.formatIntervalShort.assert_called()
		pTrackmaniaIoCotd.loadInfo.assert_called_once_with()
	# def test__buildCotdInfoMessage_estimateNext(self)
# class TestCommandCotd(unittest.TestCase)