# pylib
import re

# vendor
import minidi

class InputSanitizer(minidi.Injectable):
	def isInteger(self, s) -> bool:
		try:
			int(s)
			return True
		except BaseException:
			return False
	# def isInteger(self, s) -> bool

	def sanitize(self, dirty: str) -> str:
		return re.sub('[!@#$\'%´`"]', '', dirty)
# class InputSanitizer(minidi.Injectable)