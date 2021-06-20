# vendor
import minidi

_pTwitchBot = None

class TwitchBotWrapper(minidi.Injectable):
	def get(self):
		return _pTwitchBot
	
	def set(self, pTwitchBot):
		global _pTwitchBot
		_pTwitchBot = pTwitchBot
	# def set(self, pTwitchBot)
# class TwitchBotWrapper(minidi.Injectable)