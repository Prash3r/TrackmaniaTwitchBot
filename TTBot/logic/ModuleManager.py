# vendor
import minidi

# local
from .MariaDbWrapper import MariaDbWrapper
from .ModuleCallbackRunner import ModuleCallbackRunner

class ModuleManager(minidi.Injectable):
	pMariaDbWrapper: MariaDbWrapper
	pModuleCallbackRunner: ModuleCallbackRunner

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `modules` (\
			`channel` VARCHAR(255),\
			`ts` TIMESTAMP,\
			`luckerscounter` INT NOT NULL DEFAULT 0,\
			`joke` INT NOT NULL DEFAULT 0,\
			`kem` INT NOT NULL DEFAULT 0,\
			`mm` INT NOT NULL DEFAULT 0,\
			`roll` INT NOT NULL DEFAULT 0,\
			`score` INT NOT NULL DEFAULT 0,\
			`ooga` INT NOT NULL DEFAULT 0,\
			`ping` INT NOT NULL DEFAULT 0,\
			`test` INT NOT NULL DEFAULT 0,\
			CONSTRAINT PRIMARY KEY USING HASH (`channel`)\
		);"

		self.pMariaDbWrapper.query(query)
	# def afterInit(self)

	def _setModule(self, channelName: str, moduleName: str, minimumUserLevel: int) -> bool:
		query = f"UPDATE `modules`\
			SET `{moduleName}` = {minimumUserLevel}\
			WHERE `channel` = '{channelName}';"

		rowcount = self.pMariaDbWrapper.query(query)
		self.pModuleCallbackRunner.onModuleEnable(moduleName)
		return rowcount == 1
	# def _setModule(self, channelName: str, moduleName: str, minimumUserLevel: int) -> bool

	def activateModule(self, channelName: str, moduleName: str, minimumUserLevel: int) -> bool:
		return self._setModule(channelName, moduleName, minimumUserLevel)

	def deactivateModule(self, channelName: str, moduleName: str) -> bool:
		return self._setModule(channelName, moduleName, 0)

	def listModules(self, channelName: str) -> dict:
		query = f"SELECT *\
			FROM `modules`\
			WHERE `channel` = '{channelName}'\
			LIMIT 1;"
		rows = self.pMariaDbWrapper.fetch(query)

		if not rows:
			return {}
		
		modules = rows[0]
		del modules['channel']
		del modules['ts']
		return modules
	# def listModules(self, channelName: str) -> dict
# class ModuleManager(minidi.Injectable)