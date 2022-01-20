# vendor
import minidi

class UserLevel(minidi.Injectable):
	ADMIN = 100
	MOD = 10
	SUB = 5
	USER = 1

	NAMES = {
		ADMIN: ['admin', 'streamer', 'owner', 'camera', 'cam'],
		MOD: ['mod', 'mods', 'moderator', 'moderators', 'sword'],
		SUB: ['sub', 'subs', 'subscriber', 'subscribers'],
		USER: ['user', 'viewer', 'everyone', 'everybody']
	}

	def getUserLevelByName(self, name: str) -> int:
		for userLevel, userLevelNames in self.NAMES.items():
			if name in userLevelNames:
				return userLevel
		# for userLevel, userLevelNames in self.NAMES.items()

		return 0
	# def getUserLevelByName(self, name: str) -> int

	def getUserLevelNameByNumber(self, number: int) -> int:
		userLevelNumbers = list(self.NAMES.keys())
		userLevelNumbers = [i for i in userLevelNumbers if i <= number]
		if not userLevelNumbers:
			return '-'

		userLevelNumber = max(userLevelNumbers)
		return self.NAMES[userLevelNumber][0]
	# def getUserLevelNameByNumber(self, number: int) -> int
# class UserLevel(minidi.Injectable)