# pylib
import random

# vendor
import minidi

class Randomizer(minidi.Injectable):
	def uniformFloat(self, min: float, max: float) -> float:
		return random.uniform(min, max)

	def uniformInt(self, min: int, max: int) -> int:
		return random.randint(min, max)
# class Randomizer(minidi.Injectable)