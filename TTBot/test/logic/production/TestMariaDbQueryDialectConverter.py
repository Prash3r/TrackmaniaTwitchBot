# pylib
import unittest

# local
from TTBot.logic.production.MariaDbQueryDialectConverter import MariaDbQueryDialectConverter

class TestMariaDbQueryDialectConverter(unittest.TestCase):
	def test_convert(self):
		pMariaDbQueryDialectConverter = MariaDbQueryDialectConverter()
		query = "INSERT IGNORE INTO `modules` (`channel`, `ooga`, `ping`) VALUES (?, ?, ?)"
		self.assertEqual(pMariaDbQueryDialectConverter.convert(query), query)
	# def test_convert(self)
# class TestMariaDbQueryDialectConverter(unittest.TestCase)