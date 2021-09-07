# vendor
import minidi

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.module.ModuleList import ModuleList

class ModuleManager(minidi.Injectable):
	pDbConnector: DbConnector
	pModuleCallbackRunner: ModuleCallbackRunner
	pModuleList: ModuleList

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `modules` ( \
			`channel` VARCHAR(255), \
			`ts` TIMESTAMP, \
			PRIMARY KEY USING HASH (`channel`) \
		);"
		self.pDbConnector.execute(query)

		moduleList = self.listModules()

		moduleIds = self.pModuleList.getModuleIds()
		for moduleId in moduleIds:
			if moduleId not in moduleList:
				self._createColumn(moduleId)
		# for moduleId in moduleIds
	# def afterInit(self)

	def _createColumn(self, moduleId: str):
		# cannot use ? placeholder, but this is in control of the code -> no security risk
		query = f"ALTER TABLE `modules` ADD COLUMN `{moduleId}` INT NOT NULL DEFAULT 0;"
		self.pDbConnector.execute(query)
	# def _createColumn(self, moduleId: str)

	def _setModule(self, channelName: str, moduleId: str, minimumUserLevel: int) -> bool:
		# cannot use ? placeholder, but this is in control of the code -> no security risk
		query = f"UPDATE `modules` SET `{moduleId}` = ? WHERE `channel` = ?;"
		rowcount = self.pDbConnector.execute(query, [minimumUserLevel, channelName])
		self.pModuleCallbackRunner.onModuleEnable(moduleId)
		return rowcount == 1
	# def _setModule(self, channelName: str, moduleId: str, minimumUserLevel: int) -> bool

	def activateModule(self, channelName: str, moduleId: str, minimumUserLevel: int) -> bool:
		return self._setModule(channelName, moduleId, minimumUserLevel)

	def addChannel(self, channelName: str):
		query = "INSERT IGNORE INTO `modules` (`channel`) VALUES (?);"
		self.pDbConnector.execute(query, [channelName])
	# def addChannel(self, channelName: str)

	def deactivateModule(self, channelName: str, moduleId: str) -> bool:
		return self._setModule(channelName, moduleId, 0)

	def getChannels(self) -> list:
		query = "SELECT `channel` FROM `modules`;"
		rows = self.pDbConnector.fetch(query)
		return [row['channel'] for row in rows]
	# def getChannels(self) -> list
	
	def getMinimumAccessLevel(self, channelName: str, moduleId: str) -> int:
		# cannot use ? placeholder, but this is in control of the code -> no security risk
		query = f"SELECT `{moduleId}` FROM `modules` WHERE `channel` = ?;"
		rows = self.pDbConnector.fetch(query, [channelName])
		if ((rows[0][moduleId] == 0) or (rows[0][moduleId] == "0"):
			return 1000
		else:
			return rows[0][moduleId]
	# def getMinimumAccessLevel(self, channelName: str, moduleId: str) -> int
	
	def listModules(self) -> list:
		columns = self.pDbConnector.getColumns('modules')
		columns.remove('channel')
		columns.remove('ts')
		return columns
	# def listModules(self) -> list

	def listModulesForChannel(self, channelName: str) -> dict:
		query = "SELECT * FROM `modules` WHERE `channel` = ?"
		rows = self.pDbConnector.fetch(query, [channelName])

		if not rows:
			return {}
		
		modules = rows[0]
		del modules['channel']
		del modules['ts']
		return modules
	# def listModulesForChannel(self, channelName: str) -> dict

	def removeChannel(self, channelName: str):
		query = "DELETE FROM `modules` WHERE `channel` = ?;"
		self.pDbConnector.execute(query, [channelName])
# class ModuleManager(minidi.Injectable)