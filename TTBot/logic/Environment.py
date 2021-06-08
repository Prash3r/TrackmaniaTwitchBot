# pylib
import os

# vendor
import minidi

class Environment(minidi.Injectable):
	def getVariable(self, key: str) -> str:
		try:
			return os.environ[key]
		except KeyError:
			raise EnvironmentError(f"{key} is required to be defined in the python environment!")
	# def getVariable(self, key: str) -> str

	def getVariableWithDefault(self, key: str, default: str = '') -> str:
		return os.environ.get(key, default)
	
	def getTwitchBotUsername(self) -> str:
		return self.getVariable('TWITCH_BOT_USERNAME').lower()

	def isDebug(self) -> bool:
		return self.getVariableWithDefault('DEBUG', 'True') == 'True'
# class Environment(minidi.Injectable)