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
    
    def _activateModule(self, messageAuthorName: str, args: list[str]) -> str:
        moduleName = args[0]
        hasMinimumUserLevel = len(args) >= 2
        minimumUserLevelString = args[1] if hasMinimumUserLevel else '1'
        
        if self.pInputSanitizer.isInteger(minimumUserLevelString):
            minimumUserLevel = int(minimumUserLevelString)
            if minimumUserLevel <= 0:
                return self._deactivateModule(messageAuthorName, moduleName)
            
            minimumUserLevelString = self.pUserLevel.getUserLevelNameByNumber(minimumUserLevel)
        else:
            minimumUserLevel = self.pUserLevel.getUserLevelByName(minimumUserLevelString.lower())
            if minimumUserLevel <= 0:
                return f"Error activating module '{moduleName}', no access level '{minimumUserLevelString}' defined!"
        # if self.pInputSanitizer.isInteger(minimumUserLevelString)

        success = self.pModuleManager.activateModule(messageAuthorName, moduleName, minimumUserLevel)

        return f"Module '{moduleName}' activated with access level '{minimumUserLevelString}'!" \
            if success \
            else f"Error activating module '{moduleName}'!"
    # def _activateModule(self, messageAuthorName: str, args: list[str]) -> str

    def _deactivateModule(self, messageAuthorName: str, moduleName: str) -> str:
        success = self.pModuleManager.deactivateModule(messageAuthorName, moduleName)

        return f"Module '{moduleName}' deactivated!" \
            if success \
            else f"Error deactivating module '{moduleName}'!"
    # def _deactivateModule(self, messageAuthorName: str, moduleName: str) -> str
    
    async def execute(self, pMessage: Message, args: list[str]) -> str:
        messageAuthorName = pMessage.getAuthor().getName()
        arg = args[0].lower() if len(args) > 0 else 'list'

        if arg == 'list':
            return f"@{messageAuthorName} {self._getModulesList(messageAuthorName)}"
        elif arg == 'add' and len(args) >= 2:
            return f"@{messageAuthorName} {self._activateModule(messageAuthorName, args[1:])}"
        elif arg == 'rem' and len(args) >= 2:
            return f"@{messageAuthorName} {self._deactivateModule(messageAuthorName, args[1])}"
        else:
            return "kem1W this one needs an argument"
    # async def execute(self, pMessage: Message, args: list[str]) -> str

    def _getModulesList(self, messageAuthorName: str) -> str:
        modules = self.pModuleManager.listModulesForChannel(messageAuthorName)

        if not modules:
            return "kem1W"

        return ', '.join(
            [
                f'{moduleName}: {self.pUserLevel.getUserLevelNameByNumber(userLevel)}'
                for moduleName, userLevel in modules.items()
            ]
        )
    # def _getModulesList(self, messageAuthorName: str) -> str
# class CommandCoreModule(CommandCore)