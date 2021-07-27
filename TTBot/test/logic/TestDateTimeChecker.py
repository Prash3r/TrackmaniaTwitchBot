# pylib
import datetime
import unittest

# local
from TTBot.logic.DateTimeChecker import DateTimeChecker

class TestDateTimeChecker(unittest.TestCase):
	def test_getTimestampAge(self):
		pDateTimeChecker = DateTimeChecker()
		pTimestamp = datetime.datetime.now()
		pDelta = pDateTimeChecker.getTimestampAge(pTimestamp)
		self.assertLess(pDelta.seconds, 1)
	# def test_getTimestampAge(self)

	def test_isYoungerThan(self):
		pDateTimeChecker = DateTimeChecker()
		
		pDelta = datetime.timedelta(seconds=5)
		self.assertTrue(pDateTimeChecker.isYoungerThan(pDelta, seconds=10))

		pDelta = datetime.timedelta(hours=2, minutes=30)
		self.assertFalse(pDateTimeChecker.isYoungerThan(pDelta, hours=2, minutes=30))
	# def test_isYoungerThan(self)
# class TestDateTimeChecker(unittest.TestCase)