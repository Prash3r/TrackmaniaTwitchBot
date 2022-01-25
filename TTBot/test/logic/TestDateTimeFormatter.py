# pylib
import datetime
import unittest

# local
from TTBot.logic.DateTimeFormatter import DateTimeFormatter

class TestDateTimeFormatter(unittest.TestCase):
	def test_formatIntervalShort_Complex(self):
		pDateTimeFormatter = DateTimeFormatter()
		
		pDelta = datetime.timedelta(days=1, hours=2, minutes=3, seconds=4, milliseconds=5, microseconds=6)
		self.assertEqual('1d2h', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(hours=2, minutes=3, seconds=4, milliseconds=5, microseconds=6)
		self.assertEqual('2h3m', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(minutes=3, seconds=4, milliseconds=5, microseconds=6)
		self.assertEqual('3m4s', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(seconds=4, milliseconds=5, microseconds=6)
		self.assertEqual('4.005s', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(milliseconds=5, microseconds=6)
		self.assertEqual('5.006ms', pDateTimeFormatter.formatIntervalShort(pDelta))
		
		pDelta = datetime.timedelta(days=1, microseconds=6)
		self.assertEqual('1d', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(hours=2, microseconds=6)
		self.assertEqual('2h', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(minutes=3, microseconds=6)
		self.assertEqual('3m', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(seconds=4, microseconds=6)
		self.assertEqual('4s', pDateTimeFormatter.formatIntervalShort(pDelta))

	# def test_formatIntervalShort_Complex(self)

	def test_formatIntervalShort_Invalid(self):
		pDateTimeFormatter = DateTimeFormatter()

		pDelta = datetime.timedelta(microseconds=-1)
		self.assertRaises(ValueError, pDateTimeFormatter.formatIntervalShort, pDelta)
	# def test_formatIntervalShort_Invalid(self)

	def test_formatIntervalShort_Simple(self):
		pDateTimeFormatter = DateTimeFormatter()
		
		pDelta = datetime.timedelta()
		self.assertEqual('0.000ms', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(days=1)
		self.assertEqual('1d', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(hours=2)
		self.assertEqual('2h', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(minutes=3)
		self.assertEqual('3m', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(seconds=4)
		self.assertEqual('4s', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(milliseconds=5)
		self.assertEqual('5ms', pDateTimeFormatter.formatIntervalShort(pDelta))

		pDelta = datetime.timedelta(microseconds=6)
		self.assertEqual('0.006ms', pDateTimeFormatter.formatIntervalShort(pDelta))
	# def test_formatIntervalShort_Simple(self)
# class TestDateTimeFormatter(unittest.TestCase)