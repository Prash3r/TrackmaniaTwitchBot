# pylib
import unittest

# local
from TTBot.logic.development.SqliteQueryDialectConverter import SqliteQueryDialectConverter

class TestSqliteQueryDialectConverter(unittest.TestCase):
	def test_convert_characterSet(self):
		pSqliteQueryDialectConverter = SqliteQueryDialectConverter()
		query = "CREATE TABLE IF NOT EXISTS `modules` (`channel` VARCHAR(255) CHARACTER SET utf8, `uid` VARCHAR(32) CHARACTER SET ascii);"
		actual = pSqliteQueryDialectConverter.convert(query)
		expected = "CREATE TABLE IF NOT EXISTS `modules` (`channel` VARCHAR(255) , `uid` VARCHAR(32) );"
		self.assertEqual(actual, expected)
	# def test_convert_characterSet(self)

	def test_convert_insertIgnore(self):
		pSqliteQueryDialectConverter = SqliteQueryDialectConverter()
		query = "INSERT IGNORE INTO `modules` (`channel`) VALUES (`unittest`);"
		actual = pSqliteQueryDialectConverter.convert(query)
		expected = "INSERT OR IGNORE INTO `modules` (`channel`) VALUES (`unittest`);"
		self.assertEqual(actual, expected)
	# def test_convert_insertIgnore(self)

	def test_convert_usingHashBtree(self):
		pSqliteQueryDialectConverter = SqliteQueryDialectConverter()
		query = "CREATE TABLE IF NOT EXISTS `modules` (`channel` VARCHAR(255), `uid` VARCHAR(32), PRIMARY KEY USING HASH (`channel`), INDEX USING BTREE (`uid`));"
		actual = pSqliteQueryDialectConverter.convert(query)
		expected = "CREATE TABLE IF NOT EXISTS `modules` (`channel` VARCHAR(255), `uid` VARCHAR(32), PRIMARY KEY  (`channel`), INDEX  (`uid`));"
		self.assertEqual(actual, expected)
	# def test_convert_usingHashBtree(self)
# class TestSqliteQueryDialectConverter(unittest.TestCase)