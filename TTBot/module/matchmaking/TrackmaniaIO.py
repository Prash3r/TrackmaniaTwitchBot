# pylib
import requests

# vendor
import minidi

# local
from TTBot.logic.Environment import Environment
from .MatchmakingDataFactory import MatchmakingDataFactory

class TrackmaniaIO(minidi.Injectable):
	pEnvironment: Environment
	pMatchmakingDataFactory: MatchmakingDataFactory

	def _findPlayer(self, playerNamePart: str) -> dict:
		user_agent = {'User-agent': self.pEnvironment.getVariable('TMIO_USER_AGENT')}
		url = f'https://trackmania.io/api/players/find?search={playerNamePart}'
		resp = requests.get(url=url, headers=user_agent)
		return resp.json()
	# def _findPlayer(self, playerNamePart: str) -> dict

	def getMatchmakingData(self, playerNamePart: str) -> list:
		players = self._findPlayer(playerNamePart)
		return [self.pMatchmakingDataFactory.createFromTrackmaniaIO(player) for player in players if player['matchmaking']]
	# def getMatchmakingData(self, playerNamePart: str) -> list
# class TrackmaniaIO(minidi.Injectable)