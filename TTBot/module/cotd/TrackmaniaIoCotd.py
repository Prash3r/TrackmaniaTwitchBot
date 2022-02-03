# pylib
import requests

# vendor
import minidi

# local
from TTBot.logic.Environment import Environment
from TTBot.module.cotd.CotdInfoCache import CotdInfoCache
from TTBot.module.cotd.CotdInfoFactory import CotdInfoFactory

class TrackmaniaIoCotd(minidi.Injectable):
	pCotdInfoCache: CotdInfoCache
	pCotdInfoFactory: CotdInfoFactory
	pEnvironment: Environment

	def _getCotdInfos(self) -> list:
		user_agent = {'User-agent': self.pEnvironment.getVariable('TMIO_USER_AGENT')}
		url = 'https://trackmania.io/api/cotd/0'
		resp = requests.get(url=url, headers=user_agent)
		return resp.json()['competitions']
	# def _getCotdInfos(self) -> list

	def _getWinner(self, cotdId: int) -> str:
		user_agent = {'User-agent': self.pEnvironment.getVariable('TMIO_USER_AGENT')}
		url = f'https://trackmania.io/api/comp/{cotdId}'
		resp = requests.get(url=url, headers=user_agent)
		matches = resp.json()['rounds'][0]['matches']
		
		if not matches:
			return None

		matchDiv1Id = matches[0]['id']
		
		url = f'https://trackmania.io/api/comp/{cotdId}/match/{matchDiv1Id}/0'
		resp = requests.get(url=url, headers=user_agent)
		return resp.json()['results'][0]['player']['name']
	# def _getWinner(self, cotdId: int) -> str

	def loadInfo(self):
		cotdInfos = self._getCotdInfos()
		cotdIdsWithWinner = self.pCotdInfoCache.getIdsWithWinner(len(cotdInfos))

		for cotdInfo in cotdInfos:
			cotdId = cotdInfo['id']
			if cotdId in cotdIdsWithWinner:
				continue

			winner = self._getWinner(cotdId)
			pCotdInfo = self.pCotdInfoFactory.createFromTrackmaniaIo(cotdInfo, winner)
			self.pCotdInfoCache.write(pCotdInfo)
		# for cotdInfo in cotdInfos
	# def loadInfo(self)
# class TrackmaniaIoCotd(minidi.Injectable)