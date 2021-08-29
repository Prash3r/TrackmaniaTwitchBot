# vendor
import minidi

# local
from .InputSanitizer import InputSanitizer
from .Logger import Logger
from .MariaDbConnector import MariaDbConnector

class GlobalVariables(minidi.Injectable):
	pInputSanitizer: InputSanitizer
	pLogger: Logger
	pMariaDbConnector: MariaDbConnector

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `global_vars` (\
			`varname` VARCHAR(255),\
			`typ` VARCHAR(255),\
			`value` VARCHAR(255),\
			`ts` TIMESTAMP,\
			CONSTRAINT PRIMARY KEY USING HASH (`varname`)\
		);"
		
		self.pMariaDbConnector.query(query)
	# def afterInit(self)

	def get(self, name: str, defaultValue):
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')

		try:
			rows = self.pMariaDbConnector.fetch(f"SELECT typ, value FROM global_vars WHERE varname = '{name}' LIMIT 1;")
		except:
			self.pLogger.error(f"Retrieving process variable '{name}' failed - error in query!")
			return defaultValue
		
		if not rows:
			self.pLogger.info(f"Retrieving process variable '{name}' failed - no data in DB!")
			self._insert(name, defaultValue)
			return defaultValue
		
		row = rows[0]
		processVariableTypeString, processVariable = row['typ'], row['value']
		defaultValueType = type(defaultValue)
		defaultValueTypeString = defaultValueType.__name__

		if processVariableTypeString != defaultValueTypeString:
			self.pLogger.error(f"Mismatched type of process variable '{name}': '{processVariableTypeString}' (database) != '{defaultValueTypeString}' (default)!")
			return defaultValue
		
		return defaultValueType(processVariable)
	# def get(self, name: str, defaultValue)

	def _insert(self, name: str, value) -> bool:
		valueTypeString = type(value).__name__
		
		try:
			self.pMariaDbConnector.query(f"INSERT IGNORE INTO global_vars SET varname = '{name}', typ = '{valueTypeString}', value = '{value}';")
			return True
		except:
			self.pLogger.error(f"Could not insert process variable '{name}'!")
			return False
	# def _insert(self, name: str, value) -> bool

	def write(self, name: str, newValue) -> bool:		
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')
		
		try:
			self.pMariaDbConnector.query(f"UPDATE global_vars SET value = '{newValue}' WHERE varname = '{name}' LIMIT 1;")
			self.pLogger.debug(f"Updated process variable '{name}' to '{newValue}'!")
			return True
		except:
			self.pLogger.error(f"FAILED to update process variable '{name}' to '{newValue}'!")
			return False
	# def write(self, name: str, newValue) -> bool
# class GlobalVariables(minidi.Injectable)