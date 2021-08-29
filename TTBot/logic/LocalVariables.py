# vendor
import minidi

# local
from .InputSanitizer import InputSanitizer
from .Logger import Logger
from .MariaDbConnector import MariaDbConnector

class LocalVariables(minidi.Injectable):
	pInputSanitizer: InputSanitizer
	pLogger: Logger
	pMariaDbConnector: MariaDbConnector

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `local_vars` ( \
            `varname` varchar(255) NOT NULL, \
            `typ` varchar(255) DEFAULT NULL, \
            `value` varchar(255) DEFAULT NULL, \
            `channelname` varchar(255) DEFAULT NULL, \
            `ts` timestamp, \
            PRIMARY KEY (`varname`, `channelname`) USING HASH \
		);"
		
		self.pMariaDbConnector.query(query)
	# def afterInit(self)

	def get(self, name: str, channel: str, defaultValue):
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')
		channel = self.pInputSanitizer.sanitize(channel)
		channel = channel.replace(' ', '')

		try:
			rows = self.pMariaDbConnector.fetch(f"SELECT `typ`, `value` \
				FROM `local_vars` \
				WHERE `varname` = '{name}' AND `channelname` = '{channel}' \
				LIMIT 1; \
			")
		except:
			self.pLogger.error(f"Retrieving local variable '{name}' for channel '{channel}' failed - error in query!")
			return defaultValue
		
		if not rows:
			self.pLogger.info(f"Retrieving local variable '{name}' for channel '{channel}' failed - no data in DB!")
			self._insert(name, channel, defaultValue)
			return defaultValue
		
		row = rows[0]
		localVariableTypeString, localVariable = row['typ'], row['value']
		defaultValueType = type(defaultValue)
		defaultValueTypeString = defaultValueType.__name__

		if localVariableTypeString != defaultValueTypeString:
			self.pLogger.error(f"Mismatched type of local variable '{name}' for channel '{channel}': '{localVariableTypeString}' (database) != '{defaultValueTypeString}' (default)")
			return defaultValue
		
		return defaultValueType(localVariable)
	# def get(self, name: str, channel: str, defaultValue)

	def _insert(self, name: str, channel: str, value) -> bool:
		valueTypeString = type(value).__name__
		
		try:
			self.pMariaDbConnector.query(f"INSERT IGNORE INTO `local_vars` SET \
				`varname` = '{name}', \
				`channelname` = '{channel}', \
				`typ` = '{valueTypeString}', \
				`value` = '{value}';\
			")
			return True
		except:
			self.pLogger.error(f"Could not insert local variable '{name}' for channel '{channel}'!")
			return False
	# def _insert(self, name: str, channel: str, value) -> bool

	def write(self, name: str, channel: str, newValue) -> bool:		
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')
		channel = self.pInputSanitizer.sanitize(channel)
		channel = channel.replace(' ', '')
		
		try:
			self.pMariaDbConnector.query(f"UPDATE `local_vars` \
				SET `value` = '{newValue}' \
				WHERE `varname` = '{name}' AND `channelname` = '{channel}' \
				LIMIT 1;\
			")
			self.pLogger.debug(f"Updated local variable '{name}' for channel '{channel}' to '{newValue}'!")
			return True
		except:
			self.pLogger.error(f"FAILED to update local variable '{name}' for channel '{channel}' to '{newValue}'!")
			return False
	# def write(self, name: str, channel: str, newValue) -> bool
# class LocalVariables(minidi.Injectable)