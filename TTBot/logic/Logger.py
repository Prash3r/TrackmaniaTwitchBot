# pylib
import logging

# vendor
import minidi

class Logger(minidi.Injectable):
	### constants
	LOGGER_NAME = 'TTBot'

	### functions
	def addHandler(self, pHandler: logging.Handler):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.addHandler(pHandler)
	# def addHandler(self, pHandler: logging.Handler)

	def debug(self, msg: str):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.debug(msg)
	# def debug(self, msg: str)
	
	def error(self, msg: str):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.error(msg)
	# def error(self, msg: str)
	
	def exception(self, e: BaseException):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.exception(e)
	# def exception(self, e: BaseException)

	def getHandlers(self) -> list:
		return logging.getLogger(self.LOGGER_NAME).handlers
	
	def info(self, msg: str):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.info(msg)
	# def info(self, msg: str)

	def removeHandler(self, pHandler: logging.Handler):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.removeHandler(pHandler)
	# def removeHandler(self, pHandler: logging.Handler)

	def setLevel(self, level: int):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.setLevel(level)
	# def setLevel(self, level: int)
	
	def warning(self, msg: str):
		pLogger = logging.getLogger(self.LOGGER_NAME)
		pLogger.warning(msg)
	# def warning(self, msg: str)
# class Logger(minidi.Injectable)