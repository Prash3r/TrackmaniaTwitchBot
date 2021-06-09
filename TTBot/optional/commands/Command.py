# pylib
from abc import abstractmethod, abstractstaticmethod

# local
from ..Module import Module

class Command(Module):
	@staticmethod
	@abstractstaticmethod
	def getCommandString() -> str:
		pass
# class Command(Module)