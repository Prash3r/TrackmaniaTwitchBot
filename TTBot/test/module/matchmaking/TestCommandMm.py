# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageAuthor import MessageAuthor
from TTBot.module.matchmaking.CommandMm import CommandMm
from TTBot.module.matchmaking.MatchmakingCache import MatchmakingCache
from TTBot.module.matchmaking.MatchmakingData import MatchmakingData
from TTBot.module.matchmaking.TrackmaniaIO import TrackmaniaIO

class TestCommandMm(unittest.IsolatedAsyncioTestCase):
	async def test_getCommandTrigger(self):
		pCommandMm = CommandMm()
		self.assertListEqual(pCommandMm.getCommandTrigger(), ['matchmaking', 'mm'])
	# async def test_getCommandTrigger(self)

	async def test_getModuleId(self):
		pCommandMm = CommandMm()
		self.assertEqual(pCommandMm.getModuleId(), 'mm')
	# async def test_getModuleId(self)

	async def test__buildFullMessage(self):
		pMatchmakingData1 = MatchmakingData()
		pMatchmakingData1.setRank(1)
		pMatchmakingData1.setPlayer('unittest')
		pMatchmakingData1.setScore(1234)

		pMatchmakingData2 = MatchmakingData()
		pMatchmakingData2.setRank(42)
		pMatchmakingData2.setPlayer('TestCommandMm')
		pMatchmakingData2.setScore(789)

		matchmakingDataList = [pMatchmakingData1, pMatchmakingData2]

		pCommandMm = CommandMm()
		actualMessage = pCommandMm._buildFullMessage(matchmakingDataList)
		expectedMessage = '#1: unittest (1234 points) | #42: TestCommandMm (789 points)'
		self.assertEqual(actualMessage, expectedMessage)
	# async def test__buildFullMessage(self)

	async def test__buildSingleMessage(self):
		pMatchmakingData = MatchmakingData()
		pMatchmakingData.setRank(1)
		pMatchmakingData.setPlayer('unittest')
		pMatchmakingData.setScore(1234)

		pCommandMm = CommandMm()
		actualMessage = pCommandMm._buildSingleMessage(pMatchmakingData)
		expectedMessage = '#1: unittest (1234 points)'
		self.assertEqual(actualMessage, expectedMessage)
	# async def test__buildSingleMessage(self)

	async def test_execute_cache(self):
		pMatchmakingData1 = MatchmakingData()
		pMatchmakingData1.setRank(1)
		pMatchmakingData1.setPlayer('unittest')
		pMatchmakingData1.setScore(1234)

		pMatchmakingData2 = MatchmakingData()
		pMatchmakingData2.setRank(42)
		pMatchmakingData2.setPlayer('TestCommandMm')
		pMatchmakingData2.setScore(789)

		matchmakingDataList = [pMatchmakingData1, pMatchmakingData2]

		pMatchmakingCache = MatchmakingCache()
		pMatchmakingCache.get = mock.Mock(return_value=matchmakingDataList)
		pMatchmakingCache.write = mock.Mock()

		pTrackmaniaIO = TrackmaniaIO()
		pTrackmaniaIO.getMatchmakingData = mock.Mock(return_value=matchmakingDataList)

		pCommandMm = CommandMm()
		pCommandMm.pMatchmakingCache = pMatchmakingCache
		pCommandMm.pTrackmaniaIO = pTrackmaniaIO

		pMessage = Message(author=MessageAuthor(name='unittest'))

		actualMessage = await pCommandMm.execute(pMessage, ['test', 'kem1W'])
		expectedMessage = "@unittest #1: unittest (1234 points) | #42: TestCommandMm (789 points)"
		self.assertEqual(actualMessage, expectedMessage)

		pMatchmakingCache.get.assert_called_once_with('test')
		pMatchmakingCache.write.assert_not_called()
		pTrackmaniaIO.getMatchmakingData.assert_not_called()
	# async def test_execute_cache(self)

	async def test_execute_default(self):
		pMatchmakingData1 = MatchmakingData()
		pMatchmakingData1.setRank(1)
		pMatchmakingData1.setPlayer('unittest')
		pMatchmakingData1.setScore(1234)

		pMatchmakingData2 = MatchmakingData()
		pMatchmakingData2.setRank(42)
		pMatchmakingData2.setPlayer('TestCommandMm')
		pMatchmakingData2.setScore(789)

		matchmakingDataList = [pMatchmakingData1, pMatchmakingData2]

		pMatchmakingCache = MatchmakingCache()
		pMatchmakingCache.get = mock.Mock(return_value=matchmakingDataList)
		pMatchmakingCache.write = mock.Mock()

		pTrackmaniaIO = TrackmaniaIO()
		pTrackmaniaIO.getMatchmakingData = mock.Mock(return_value=matchmakingDataList)

		pCommandMm = CommandMm()
		pCommandMm.pMatchmakingCache = pMatchmakingCache
		pCommandMm.pTrackmaniaIO = pTrackmaniaIO

		pMessage = Message(author=MessageAuthor(name='unittest'))

		actualMessage = await pCommandMm.execute(pMessage, [])
		expectedMessage = "@unittest Missing a player name (or part of a players name)!"
		self.assertEqual(actualMessage, expectedMessage)

		pMatchmakingCache.get.assert_not_called()
		pMatchmakingCache.write.assert_not_called()
		pTrackmaniaIO.getMatchmakingData.assert_not_called()
	# async def test_execute_default(self)

	async def test_execute_tmio_failure(self):
		pMatchmakingCache = MatchmakingCache()
		pMatchmakingCache.get = mock.Mock(return_value=[])
		pMatchmakingCache.write = mock.Mock()

		pTrackmaniaIO = TrackmaniaIO()
		pTrackmaniaIO.getMatchmakingData = mock.Mock(return_value=[])

		pCommandMm = CommandMm()
		pCommandMm.pMatchmakingCache = pMatchmakingCache
		pCommandMm.pTrackmaniaIO = pTrackmaniaIO

		pMessage = Message(author=MessageAuthor(name='unittest'))

		actualMessage = await pCommandMm.execute(pMessage, ['test', 'kem1W'])
		expectedMessage = "@unittest No player found in TM2020 matchmaking resembling the name 'test'!"
		self.assertEqual(actualMessage, expectedMessage)

		pMatchmakingCache.get.assert_called_once_with('test')
		pMatchmakingCache.write.assert_not_called()
		pTrackmaniaIO.getMatchmakingData.assert_called_once_with('test')
	# async def test_execute_tmio_failure(self)

	async def test_execute_tmio_success(self):
		pMatchmakingData1 = MatchmakingData()
		pMatchmakingData1.setRank(1)
		pMatchmakingData1.setPlayer('unittest')
		pMatchmakingData1.setScore(1234)

		pMatchmakingData2 = MatchmakingData()
		pMatchmakingData2.setRank(42)
		pMatchmakingData2.setPlayer('TestCommandMm')
		pMatchmakingData2.setScore(789)

		matchmakingDataList = [pMatchmakingData1, pMatchmakingData2]

		pMatchmakingCache = MatchmakingCache()
		pMatchmakingCache.get = mock.Mock(return_value=[])
		pMatchmakingCache.write = mock.Mock()

		pTrackmaniaIO = TrackmaniaIO()
		pTrackmaniaIO.getMatchmakingData = mock.Mock(return_value=matchmakingDataList)

		pCommandMm = CommandMm()
		pCommandMm.pMatchmakingCache = pMatchmakingCache
		pCommandMm.pTrackmaniaIO = pTrackmaniaIO

		pMessage = Message(author=MessageAuthor(name='unittest'))

		actualMessage = await pCommandMm.execute(pMessage, ['test', 'kem1W'])
		expectedMessage = "@unittest #1: unittest (1234 points) | #42: TestCommandMm (789 points)"
		self.assertEqual(actualMessage, expectedMessage)

		pMatchmakingCache.get.assert_called_once_with('test')
		pMatchmakingCache.write.assert_any_call(pMatchmakingData1)
		pMatchmakingCache.write.assert_any_call(pMatchmakingData2)
		pTrackmaniaIO.getMatchmakingData.assert_called_once_with('test')
	# async def test_execute_tmio_success(self)
# class TestCommandMm(unittest.IsolatedAsyncioTestCase)