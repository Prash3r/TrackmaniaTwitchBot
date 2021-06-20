# pylib
import datetime

class MatchmakingData:
	def __init__(self):
		self._player = ''
		self._playerAccountId = ''
		self._pTimestamp = None
		self._rank = 0
		self._score = 0
	# def __init__(self)

	def getPlayer(self) -> str:
		return self._player

	def getPlayerAccountId(self) -> str:
		return self._playerAccountId
	
	def getRank(self) -> int:
		return self._rank
	
	def getTimestamp(self) -> datetime.datetime:
		return self._pTimestamp
	
	def getScore(self) -> int:
		return self._score
	
	def setPlayer(self, player: str):
		self._player = player
	
	def setPlayerAccountId(self, playerAccountId: str):
		self._playerAccountId = playerAccountId
	
	def setRank(self, rank: int):
		self._rank = rank
	
	def setTimestamp(self, pTimestamp: datetime.datetime):
		self._pTimestamp = pTimestamp
	
	def setScore(self, score: int):
		self._score = score
# class MatchmakingData