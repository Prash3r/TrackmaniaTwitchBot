# local
from TTBot.data.Message import Message
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.ModuleManager import ModuleManager
from TTBot.logic.UserLevel import UserLevel
from TTBot.module.core.CommandCore import CommandCore

class CommandCoreModule(CommandCore):
    pInputSanitizer: InputSanitizer
    pModuleManager: ModuleManager
    pUserLevel: UserLevel

    def getCommandTrigger(self):
        return 'module'
    
    def _activateModule(self, channelName: str, args: list[str]) -> str:
        moduleName = args[0]
        hasMinimumUserLevel = len(args) >= 2
        minimumUserLevelString = args[1] if hasMinimumUserLevel else '1'
        
        if self.pInputSanitizer.isInteger(minimumUserLevelString):
            minimumUserLevel = int(minimumUserLevelString)
            if minimumUserLevel <= 0:
                return self._deactivateModule(channelName, moduleName)
            
            minimumUserLevelString = self.pUserLevel.getUserLevelNameByNumber(minimumUserLevel)
        else:
            minimumUserLevel = self.pUserLevel.getUserLevelByName(minimumUserLevelString.lower())
            if minimumUserLevel <= 0:
                return f"Error activating module '{moduleName}', no access level '{minimumUserLevelString}' defined!"
        # if self.pInputSanitizer.isInteger(minimumUserLevelString)

        success = self.pModuleManager.activateModule(channelName, moduleName, minimumUserLevel)

        return f"Module '{moduleName}' activated with access level '{minimumUserLevelString}'!" \
            if success \
            else f"Error activating module '{moduleName}'!"
    # def _activateModule(self, channelName: str, args: list[str]) -> str

    def _deactivateModule(self, channelName: str, moduleName: str) -> str:
        success = self.pModuleManager.deactivateModule(channelName, moduleName)

        return f"Module '{moduleName}' deactivated!" \
            if success \
            else f"Error deactivating module '{moduleName}'!"
    # def _deactivateModule(self, channelName: str, moduleName: str) -> str
    
    async def execute(self, pMessage: Message, args: list[str]) -> str:
        channelName = pMessage.getChannel().getName()
        messageAuthorName = pMessage.getAuthor().getName()
        arg = args[0].lower() if len(args) > 0 else 'list'

        if arg == 'list':
            return f"@{messageAuthorName} {self._getModulesList(channelName)}"
        elif arg == 'add' and len(args) >= 2:
            return f"@{messageAuthorName} {self._activateModule(channelName, args[1:])}"
        elif arg == 'rem' and len(args) >= 2:
            return f"@{messageAuthorName} {self._deactivateModule(channelName, args[1])}"
        else:
            return "kem1W this one needs an argument"
    # async def execute(self, pMessage: Message, args: list[str]) -> str

    def _getModulesList(self, channelName: str) -> str:
        modules = self.pModuleManager.listModulesForChannel(channelName)

        if not modules:
            return "kem1W"

        return ', '.join(
            [
                f'{moduleName}: {self.pUserLevel.getUserLevelNameByNumber(userLevel)}'
                for moduleName, userLevel in modules.items()
            ]
        )
    # def _getModulesList(self, channelName: str) -> str
# class CommandCoreModule(CommandCore)