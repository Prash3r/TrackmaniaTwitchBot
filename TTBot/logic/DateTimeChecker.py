# pylib
import datetime

# vendor
import minidi

class DateTimeChecker(minidi.Injectable):
	def getTimestampAge(self, pTimestamp: datetime.datetime):
		return datetime.datetime.now() - pTimestamp
	
	def isYoungerThan(self, pDelta: datetime.timedelta, **kwargs):
		return pDelta < datetime.timedelta(**kwargs)
# class DateTimeChecker(minidi.Injectable)