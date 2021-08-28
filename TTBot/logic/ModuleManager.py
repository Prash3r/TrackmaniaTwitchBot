# vendor
import minidi

# local
from .MariaDbConnector import MariaDbConnector
from .ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.optional.ModuleList import ModuleList

class ModuleManager(minidi.Injectable):
	pMariaDbConnector: MariaDbConnector
	pModuleCallbackRunner: ModuleCallbackRunner
	pModuleList: ModuleList

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `modules` (\
			`channel` VARCHAR(255),\
			`ts` TIMESTAMP,\
			CONSTRAINT PRIMARY KEY USING HASH (`channel`)\
		);"
		self.pMariaDbConnector.query(query)

		moduleList = self.listModules()

		moduleIds = self.pModuleList.getAllModuleIds()
		for moduleId in moduleIds:
			if moduleId not in moduleList:
				self._createColumn(moduleId)
		# for moduleId in moduleIds
	# def afterInit(self)

	def _createColumn(self, moduleId: str):
		query = f"ALTER TABLE `modules`\
			ADD COLUMN `{moduleId}` INT NOT NULL DEFAULT 0;"
		
		self.pMariaDbConnector.query(query)
	# def _createColumn(self, moduleId: str)

	def _setModule(self, channelName: str, moduleName: str, minimumUserLevel: int) -> bool:
		query = f"UPDATE `modules`\
			SET `{moduleName}` = {minimumUserLevel}\
			WHERE `channel` = '{channelName}';"

		rowcount = self.pMariaDbConnector.query(query)
		self.pModuleCallbackRunner.onModuleEnable(moduleName)
		return rowcount == 1
	# def _setModule(self, channelName: str, moduleName: str, minimumUserLevel: int) -> bool

	def activateModule(self, channelName: str, moduleName: str, minimumUserLevel: int) -> bool:
		return self._setModule(channelName, moduleName, minimumUserLevel)

	def deactivateModule(self, channelName: str, moduleName: str) -> bool:
		return self._setModule(channelName, moduleName, 0)
	
	def listModules(self) -> list:
		rows = self.pMariaDbConnector.query("SHOW FIELDS FROM `modules`;")
		return [row['Field'] for row in rows]
	# def listModules(self) -> list

	def listModulesForChannel(self, channelName: str) -> dict:
		query = f"SELECT *\
			FROM `modules`\
			WHERE `channel` = '{channelName}'\
			LIMIT 1;"
		rows = self.pMariaDbConnector.fetch(query)

		if not rows:
			return {}
		
		modules = rows[0]
		del modules['channel']
		del modules['ts']
		return modules
	# def listModulesForChannel(self, channelName: str) -> dict
# class ModuleManager(minidi.Injectable)