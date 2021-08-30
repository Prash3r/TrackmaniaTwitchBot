# vendor
import minidi

# local
from .DbConnector import DbConnector
from .ModuleCallbackRunner import ModuleCallbackRunner
from TTBot.optional.ModuleList import ModuleList

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

		moduleIds = self.pModuleList.getAllModuleIds()
		for moduleId in moduleIds:
			if moduleId not in moduleList:
				self._createColumn(moduleId)
		# for moduleId in moduleIds
	# def afterInit(self)

	def _createColumn(self, moduleId: str):
		query = f"ALTER TABLE `modules` \
			ADD COLUMN `{moduleId}` INT NOT NULL DEFAULT 0;"
		
		self.pDbConnector.execute(query)
	# def _createColumn(self, moduleId: str)

	def _setModule(self, channelName: str, moduleId: str, minimumUserLevel: int) -> bool:
		query = f"UPDATE `modules`\
			SET `{moduleId}` = {minimumUserLevel}\
			WHERE `channel` = '{channelName}';"

		rowcount = self.pDbConnector.execute(query)
		self.pModuleCallbackRunner.onModuleEnable(moduleId)
		return rowcount == 1
	# def _setModule(self, channelName: str, moduleId: str, minimumUserLevel: int) -> bool

	def activateModule(self, channelName: str, moduleId: str, minimumUserLevel: int) -> bool:
		return self._setModule(channelName, moduleId, minimumUserLevel)

	def addChannel(self, channelName: str):
		self.pDbConnector.execute(f"INSERT IGNORE INTO `modules` (`channel`) VALUES ('{channelName}');")

	def deactivateModule(self, channelName: str, moduleId: str) -> bool:
		return self._setModule(channelName, moduleId, 0)

	def getChannels(self) -> list:
		rows = self.pDbConnector.fetch("SELECT `channel` FROM `modules`;")
		return [row['channel'] for row in rows]
	# def getChannels(self) -> list
	
	def getMinimumAccessLevel(self, channelName: str, moduleId: str) -> int:
		rows = self.pDbConnector.fetch(f"SELECT `{moduleId}` FROM `modules` WHERE `channel` = '{channelName}' LIMIT 1;")
		return rows[0][moduleId]
	# def getMinimumAccessLevel(self, channelName: str, moduleId: str) -> int
	
	def listModules(self) -> list:
		columns = self.pDbConnector.getColumns('modules')
		columns.remove('channel')
		columns.remove('ts')
		return columns
	# def listModules(self) -> list

	def listModulesForChannel(self, channelName: str) -> dict:
		query = f"SELECT * \
			FROM `modules` \
			WHERE `channel` = '{channelName}' \
			LIMIT 1;"
		rows = self.pDbConnector.fetch(query)

		if not rows:
			return {}
		
		modules = rows[0]
		del modules['channel']
		del modules['ts']
		return modules
	# def listModulesForChannel(self, channelName: str) -> dict
# class ModuleManager(minidi.Injectable)