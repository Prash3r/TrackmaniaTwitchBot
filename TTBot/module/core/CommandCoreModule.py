# local
from TTBot.module.core.CommandCore import CommandCore
from TTBot.data.Message import Message
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.ModuleManager import ModuleManager

class CommandCoreModule(CommandCore):
    pInputSanitizer: InputSanitizer
    pModuleManager: ModuleManager

    def getCommandString(self) -> str:
        return 'module'
    
    def _activateModule(self, messageAuthorName: str, args: list) -> str:
        moduleName = args[0]
        hasMinimumUserLevel = len(args) >= 2 and self.pInputSanitizer.isInteger(args[1])
        minimumUserLevel = args[1] if hasMinimumUserLevel else 1

        if minimumUserLevel <= 0:
            return self._deactivateModule(messageAuthorName, moduleName)

        success = self.pModuleManager.activateModule(messageAuthorName, moduleName, minimumUserLevel)

        return f"Module '{moduleName}' activated with access level {minimumUserLevel}!" \
            if success \
            else f"Error activating module '{moduleName}!"
    # def _activateModule(self, messageAuthorName: str, args: list) -> str

    def _deactivateModule(self, messageAuthorName: str, moduleName: str) -> str:
        success = self.pModuleManager.deactivateModule(messageAuthorName, moduleName)

        return f"Module '{moduleName}' deactivated!" \
            if success \
            else f"Error deactivating module '{moduleName}!"
    # def _deactivateModule(self, messageAuthorName: str, moduleName: str) -> str
    
    async def execute(self, pMessage: Message, args: list) -> str:
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
    # async def execute(self, pMessage: Message, args: list) -> str

    def _getModulesList(self, messageAuthorName: str) -> str:
        modules = self.pModuleManager.listModulesForChannel(messageAuthorName)

        if not modules:
            return "kem1W"

        return ', '.join([f'{moduleName}: {userLevel}' for moduleName, userLevel in modules.items()])
    # def _getModulesList(self, messageAuthorName: str) -> str
# class CommandCoreModule(CommandCore)