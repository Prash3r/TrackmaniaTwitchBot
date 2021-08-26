# local
from ..Command import Command

class CommandCore(Command):
    def getRightsId(self) -> str:
        return 'core'
# class CommandCore(Command)