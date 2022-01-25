# pylib
import datetime

class CotdInfo:
	def __init__(self):
		self._id: int = -1
		self._name: str = ''
		self._numPlayers: int = 0
		self._pDateStart: datetime.datetime = None
		self._pDateEnd: datetime.datetime = None
		self._winner: str = None
	# def __init__(self)

	def getDateEnd(self) -> datetime.datetime:
		return self._pDateEnd
	
	def getDateStart(self) -> datetime.datetime:
		return self._pDateStart
	
	def getId(self) -> int:
		return self._id
	
	def getName(self) -> str:
		return self._name
	
	def getNumPlayers(self) -> int:
		return self._numPlayers
	
	def getWinner(self) -> str:
		return self._winner
	
	def setDateEnd(self, pDateEnd: datetime.datetime):
		self._pDateEnd = pDateEnd
	
	def setDateStart(self, pDateStart: datetime.datetime):
		self._pDateStart = pDateStart
	
	def setId(self, _id: int):
		self._id = _id
	
	def setName(self, name: str):
		self._name = name
	
	def setNumPlayers(self, numPlayers: int):
		self._numPlayers = numPlayers
	
	def setWinner(self, winner: str):
		self._winner = winner
# class CotdData