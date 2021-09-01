# pylib
from abc import abstractmethod

# vendor
import minidi

class DbQueryDialectConverter(minidi.Injectable):
	@abstractmethod
	def convert(self, query: str) -> str:
		pass
# class DbQueryDialectConverter(minidi.Injectable)