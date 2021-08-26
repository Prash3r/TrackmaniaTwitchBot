# local
from .CommandCore import CommandCore
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.MariaDbWrapper import MariaDbWrapper
from TTBot.logic.TwitchMessageEvaluator import TwitchMessageEvaluator
from TTBot.optional.ModuleCallbackRunner import ModuleCallbackRunner

class CommandCoreModule(CommandCore):
    pInputSanitizer: InputSanitizer
    pMariaDbWrapper: MariaDbWrapper
    pModuleCallbackRunner: ModuleCallbackRunner
    pTwitchMessageEvaluator: TwitchMessageEvaluator

    def getCommandString(self) -> str:
        return 'module'
    
    def _activateModule(self, messageAuthorName: str, args: list) -> str:
        moduleName = args[0]
        hasMinimumUserLevel = len(args) >= 2 and self.pInputSanitizer.isInteger(args[1])
        minimumUserLevel = args[1] if hasMinimumUserLevel else 1

        if minimumUserLevel <= 0:
            return self._deactivateModule(messageAuthorName, moduleName)

        success = self.pModuleCallbackRunner.onModuleEnable(moduleName)
        if not success:
            return f"Error activating module '{moduleName}!"

        self.pMariaDbWrapper.query(f"UPDATE modules SET `{moduleName}` = {minimumUserLevel} WHERE channel = '{messageAuthorName}';")
        return f"Module '{moduleName}' activated with access level {minimumUserLevel}!"
    # def _activateModule(self, messageAuthorName: str, args: list) -> str

    def _deactivateModule(self, messageAuthorName: str, moduleName: str) -> str:
        success = self.pModuleCallbackRunner.onModuleDisable(moduleName)
        if not success:
            return f"Error deactivating module '{moduleName}!"

        self.pMariaDbWrapper.query(f"UPDATE modules SET `{moduleName}` = 0 WHERE channel = '{messageAuthorName}';")
        return f"Module '{moduleName}' deactivated!"
    # def _deactivateModule(self, messageAuthorName: str, moduleName: str) -> str
    
    async def execute(self, pMessage, args: list) -> str:
        messageAuthorName = self.pTwitchMessageEvaluator.getAuthorName(pMessage)
        if len(args) > 0:
            arg = args[0].lower()
        else:
            arg = 'list'

        if arg == 'list':
            return f"@{messageAuthorName} {self._getModulesList(messageAuthorName)}"
        elif arg == 'add' and len(args) >= 2:
            return f"@{messageAuthorName} {self._activateModule(messageAuthorName, args[1:])}"
        elif arg == 'rem' and len(args) >= 2:
            return f"@{messageAuthorName} {self._deactivateModule(messageAuthorName, args[1])}"
        else:
            return "kem1W this one needs an argument"
    # async def execute(self, pMessage, args: list) -> str

    def _getModulesList(self, messageAuthorName: str) -> str:
        rows = self.pMariaDbWrapper.fetch(f"SELECT * FROM modules WHERE channel = '{messageAuthorName}' LIMIT 1;")
        if not rows:
            return "kem1W"
        
        output = []
        row = rows[0]
        for moduleName, userLevel in row.items():
            if moduleName in ['channel', 'ts']:
                continue

            output.append(f"{moduleName}: {userLevel}")
        # for moduleName, userLevel in row.items()

        return ', '.join(output)
    # def _getModulesList(self, messageAuthorName: str) -> str
# class CommandCoreModule(CommandCore)