# pylib
import unittest

# local
from TTBot.logic.InputSanitizer import InputSanitizer

class TestInputSanitizer(unittest.TestCase):
	def test_isInteger(self):
		pInputSanitizer = InputSanitizer()
		self.assertTrue(pInputSanitizer.isInteger(0))
		self.assertTrue(pInputSanitizer.isInteger(1))
		self.assertTrue(pInputSanitizer.isInteger(-1))
		self.assertTrue(pInputSanitizer.isInteger('0'))
		self.assertTrue(pInputSanitizer.isInteger('1'))
		self.assertTrue(pInputSanitizer.isInteger('-1'))
		self.assertTrue(pInputSanitizer.isInteger(0.5))
		self.assertTrue(pInputSanitizer.isInteger(False))
		self.assertTrue(pInputSanitizer.isInteger(True))
		self.assertTrue(pInputSanitizer.isInteger(int()))

		self.assertFalse(pInputSanitizer.isInteger(int))
		self.assertFalse(pInputSanitizer.isInteger('0.5'))
		self.assertFalse(pInputSanitizer.isInteger('hello'))
		self.assertFalse(pInputSanitizer.isInteger('4asdf'))
		self.assertFalse(pInputSanitizer.isInteger(float('NaN')))
		self.assertFalse(pInputSanitizer.isInteger(object()))
	# def test_isInteger(self)

	def test_sanitize(self):
		pInputSanitizer = InputSanitizer()
		self.assertEqual(pInputSanitizer.sanitize('Hello, World!'), 'Hello, World')
		self.assertEqual(pInputSanitizer.sanitize('\'; SQL injection --'), '; SQL injection --')
		self.assertEqual(pInputSanitizer.sanitize('@unittest'), 'unittest')
		self.assertEqual(pInputSanitizer.sanitize('Rank #1'), 'Rank 1')
		self.assertEqual(pInputSanitizer.sanitize('${eval(alert("injected"))}'), '{eval(alert(injected))}')
		self.assertEqual(pInputSanitizer.sanitize('`tablename_escaping`'), 'tablename_escaping')
		self.assertEqual(pInputSanitizer.sanitize('%2d %5s'), '2d 5s')
	# def test_sanitize(self)
# class TestInputSanitizer(unittest.TestCase)