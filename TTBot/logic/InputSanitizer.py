# pylib
import re

# vendor
import minidi

class InputSanitizer(minidi.Injectable):
	def sanitize(self, dirty: str) -> str:
		return re.sub('[!@#$\'%´`"]', '', dirty)
# class InputSanitizer(minidi.Injectable)