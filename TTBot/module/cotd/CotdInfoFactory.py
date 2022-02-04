# pylib
import datetime

# vendor
import minidi

# local
from TTBot.module.cotd.CotdInfo import CotdInfo

class CotdInfoFactory(minidi.Injectable):
	def createFromCacheQuery(self, dataInfo: dict) -> CotdInfo:
		if isinstance(dataInfo['date_start'], str):
			dataInfo['date_start'] = datetime.datetime.fromisoformat(dataInfo['date_start'])
		if isinstance(dataInfo['date_end'], str):
			dataInfo['date_end'] = datetime.datetime.fromisoformat(dataInfo['date_end'])

		pCotdInfo = CotdInfo()
		pCotdInfo.setId(dataInfo['id'])
		pCotdInfo.setName(dataInfo['name'])
		pCotdInfo.setNumPlayers(dataInfo['num_players'])
		pCotdInfo.setDateStart(dataInfo['date_start'])
		pCotdInfo.setDateEnd(dataInfo['date_end'])
		pCotdInfo.setWinner(dataInfo['winner'])
		return pCotdInfo
	# def createFromCacheQuery(self, dataInfo: dict) -> CotdInfo

	def createFromTrackmaniaIo(self, dataInfo: dict, winner: str) -> CotdInfo:
		pDateStart = datetime.datetime.utcfromtimestamp(dataInfo['starttime'])
		pDateEnd = datetime.datetime.utcfromtimestamp(dataInfo['endtime'])

		pCotdInfo = CotdInfo()
		pCotdInfo.setId(dataInfo['id'])
		pCotdInfo.setName(dataInfo['name'])
		pCotdInfo.setNumPlayers(dataInfo['players'])
		pCotdInfo.setDateStart(pDateStart)
		pCotdInfo.setDateEnd(pDateEnd)
		pCotdInfo.setWinner(winner)
		return pCotdInfo
	# def createFromTrackmaniaIo(self, dataInfo: dict, winner: str) -> CotdInfo

	def createNext(self, pCotdInfoPrev: CotdInfo) -> CotdInfo:
		# add 8 hours to estimate next event start & end
		# add 10 minutes to account for possible early start of pCotdInfoPrev
		pDelta = datetime.timedelta(hours=8, minutes=10)

		pDateStart = pCotdInfoPrev.getDateStart() + pDelta
		pRoundDownToFullHour = datetime.timedelta(
			minutes=pDateStart.minute,
			seconds=pDateStart.second,
			microseconds=pDateStart.microsecond
		)
		pDateStart -= pRoundDownToFullHour

		pDateEnd = pCotdInfoPrev.getDateEnd() + pDelta
		pRoundDownToFullHour = datetime.timedelta(
			minutes=pDateEnd.minute,
			seconds=pDateEnd.second,
			microseconds=pDateEnd.microsecond
		)
		pDateEnd -= pRoundDownToFullHour

		pCotdInfoNext = CotdInfo()
		pCotdInfoNext.setDateStart(pDateStart)
		pCotdInfoNext.setDateEnd(pDateEnd)
		return pCotdInfoNext
	# def createNext(self, pCotdInfoPrev: CotdInfo) -> CotdInfo
# class CotdInfoFactory(minidi.Injectable)