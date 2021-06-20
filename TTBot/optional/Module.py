# pylib
from abc import abstractmethod

# vendor
import minidi

class Module(minidi.Injectable):
	@abstractmethod
	def getRightsId(self) -> str:
		pass
# class Module(minidi.Injectable)