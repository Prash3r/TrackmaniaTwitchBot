# vendor
import minidi

# local
from TTBot.logic.DbConnector import DbConnector
from TTBot.logic.InputSanitizer import InputSanitizer
from TTBot.logic.Logger import Logger

class LocalVariables(minidi.Injectable):
	pDbConnector: DbConnector
	pInputSanitizer: InputSanitizer
	pLogger: Logger

	def afterInit(self):
		query = "CREATE TABLE IF NOT EXISTS `local_vars` ( \
            `varname` varchar(255) NOT NULL, \
            `typ` varchar(255) DEFAULT NULL, \
            `value` varchar(255) DEFAULT NULL, \
            `channelname` varchar(255) DEFAULT NULL, \
            `ts` timestamp, \
            PRIMARY KEY (`varname`, `channelname`) USING HASH \
		);"
		
		self.pDbConnector.execute(query)
	# def afterInit(self)

	def get(self, name: str, channel: str, defaultValue):
		name = self.pInputSanitizer.sanitize(name)
		name = name.replace(' ', '')
		channel = self.pInputSanitizer.sanitize(channel)
		channel = channel.replace(' ', '')

		try:
			query = "SELECT `typ`, `value` FROM `local_vars` WHERE `varname` = ? AND `channelname` = ?;"
			rows = self.pDbConnector.fetch(query, [name, channel])
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
			query = "INSERT IGNORE INTO `local_vars` (`varname`, `channelname`, `typ`, `value`) VALUES (?, ?, ?, ?);"
			self.pDbConnector.execute(query, [name, channel, valueTypeString, value])
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
			query = "UPDATE `local_vars` SET `value` = ? WHERE `varname` = ? AND `channelname` = ?;"
			self.pDbConnector.execute(query, [newValue, name, channel])
			self.pLogger.debug(f"Updated local variable '{name}' for channel '{channel}' to '{newValue}'!")
			return True
		except:
			self.pLogger.error(f"FAILED to update local variable '{name}' for channel '{channel}' to '{newValue}'!")
			return False
	# def write(self, name: str, channel: str, newValue) -> bool
# class LocalVariables(minidi.Injectable)