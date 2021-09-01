# vendor
import minidi

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger

class GlobalVariables(minidi.Injectable):
	pDbConnector: DbConnector
	pInputSanitizer: InputSanitizer
	pLogger: Logger

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `global_vars` ( \
			`varname` VARCHAR(255), \
			`typ` VARCHAR(255), \
			`value` VARCHAR(255), \
			`ts` TIMESTAMP, \
			PRIMARY KEY USING HASH (`varname`) \
		);"
		
		self.pDbConnector.execute(query)
	# def afterInit(self)

	def get(self, name: str, defaultValue):
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')

		try:
			rows = self.pDbConnector.fetch(f" \
				SELECT `typ`, `value` \
				FROM `global_vars` \
				WHERE `varname` = '{name}' \
				LIMIT 1; \
			")
		except:
			self.pLogger.error(f"Retrieving global variable '{name}' failed - error in query!")
			return defaultValue
		
		if not rows:
			self.pLogger.info(f"Retrieving global variable '{name}' failed - no data in DB!")
			self._insert(name, defaultValue)
			return defaultValue
		
		row = rows[0]
		globalVariableTypeString, globalVariable = row['typ'], row['value']
		defaultValueType = type(defaultValue)
		defaultValueTypeString = defaultValueType.__name__

		if globalVariableTypeString != defaultValueTypeString:
			self.pLogger.error(f"Mismatched type of global variable '{name}': '{globalVariableTypeString}' (database) != '{defaultValueTypeString}' (default)")
			return defaultValue
		
		return defaultValueType(globalVariable)
	# def get(self, name: str, defaultValue)

	def _insert(self, name: str, value) -> bool:
		valueTypeString = type(value).__name__
		
		try:
			self.pDbConnector.execute(f" \
				INSERT IGNORE INTO `global_vars` (`varname`, `typ`, `value`) \
				VALUES ('{name}', '{valueTypeString}', '{value}'); \
			")
			return True
		except:
			self.pLogger.error(f"Could not insert global variable '{name}'!")
			return False
	# def _insert(self, name: str, value) -> bool

	def write(self, name: str, newValue) -> bool:		
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')
		
		try:
			self.pDbConnector.execute(f" \
				UPDATE `global_vars` \
				SET `value` = '{newValue}' \
				WHERE `varname` = '{name}'; \
			")
			self.pLogger.debug(f"Updated global variable '{name}' to '{newValue}'!")
			return True
		except:
			self.pLogger.error(f"FAILED to update global variable '{name}' to '{newValue}'!")
			return False
	# def write(self, name: str, newValue) -> bool
# class GlobalVariables(minidi.Injectable)