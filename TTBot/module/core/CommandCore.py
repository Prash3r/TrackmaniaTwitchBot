# local
from TTBot.module.Command import Command

class CommandCore(Command):
    def getModuleId(self) -> str:
        return 'core'
# class CommandCore(Command)