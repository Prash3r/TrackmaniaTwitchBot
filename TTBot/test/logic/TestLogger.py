# pylib
import logging
import os
import unittest

# local
from TTBot.logic.Logger import Logger

class TestLogger(unittest.TestCase):
	pFileHandler: logging.FileHandler
	pLogger: Logger
	index: int

	@classmethod
	def setUpClass(cls):
		cls.index = 0
		return super().setUpClass()
	# def setUpClass(cls)

	def setUp(self):
		self.pFileHandler = logging.FileHandler(f'./TestLogger.{TestLogger.index}.log')
		self.pLogger = Logger()
		self.pLogger.addHandler(self.pFileHandler)
		return super().setUp()
	# def setUp(self)

	def tearDown(self) -> None:
		self.pFileHandler.flush()
		self.pFileHandler.close()
		self.pLogger.removeHandler(self.pFileHandler)
		return super().tearDown()
	# def tearDown(self) -> None

	@classmethod
	def tearDownClass(cls):
		for i in range(cls.index):
			filename = f'./TestLogger.{i}.log'
			if os.path.isfile(filename):
				os.remove(filename)
		# for i in range(cls.index)

		return super().tearDownClass()
	# def tearDownClass(cls)

	def processTestLoggerLog(self) -> list:
		lines = []
		with open(f'./TestLogger.{TestLogger.index}.log') as pFile:
			lines = pFile.read().splitlines()
			pFile.close()
		
		TestLogger.index += 1
		return lines
	# def processTestLoggerLog(self) -> list

	def test_addHandler(self):
		# there always is one handler in this unittest
		self.assertEqual(len(self.pLogger.getHandlers()), 1)

		pStreamHandler = logging.StreamHandler()
		self.pLogger.addHandler(pStreamHandler)
		self.assertEqual(len(self.pLogger.getHandlers()), 2)

		self.pLogger.removeHandler(pStreamHandler)
		self.assertEqual(len(self.pLogger.getHandlers()), 1)
	# def test_addHandler(self)

	def test_debug_1(self):
		self.pLogger.setLevel(logging.DEBUG)
		self.pLogger.debug('Hello, World!')
		log = self.processTestLoggerLog()
		expected = ['Hello, World!']
		self.assertListEqual(log, expected)
	# def test_debug_1(self)

	def test_debug_2(self):
		self.pLogger.setLevel(logging.INFO)
		self.pLogger.debug('Hello, World!')
		log = self.processTestLoggerLog()
		expected = []
		self.assertListEqual(log, expected)
	# def test_debug_2(self)

	def test_error_1(self):
		self.pLogger.setLevel(logging.ERROR)
		self.pLogger.error('Hello, World!')
		log = self.processTestLoggerLog()
		expected = ['Hello, World!']
		self.assertListEqual(log, expected)
	# def test_error_1(self)

	def test_error_2(self):
		self.pLogger.setLevel(logging.CRITICAL)
		self.pLogger.error('Hello, World!')
		log = self.processTestLoggerLog()
		expected = []
		self.assertListEqual(log, expected)
	# def test_error_2(self)

	def test_exception_1(self):
		self.pLogger.setLevel(logging.ERROR)
		self.pLogger.exception(ValueError('Some Error'))

		log = self.processTestLoggerLog()
		expected = [
			'Some Error',
			'NoneType: None'
		]
		self.assertListEqual(log, expected)
	# def test_exception_1(self)

	def test_exception_2(self):
		self.pLogger.setLevel(logging.CRITICAL)
		self.pLogger.exception(ValueError('Some Error'))

		log = self.processTestLoggerLog()
		expected = []
		self.assertListEqual(log, expected)
	# def test_exception_2(self)

	def test_getHandlers(self):
		# there always is one handler in this unittest
		self.assertEqual(len(self.pLogger.getHandlers()), 1)
	# def test_getHandlers(self)

	def test_info_1(self):
		self.pLogger.setLevel(logging.INFO)
		self.pLogger.info('Hello, World!')
		log = self.processTestLoggerLog()
		expected = ['Hello, World!']
		self.assertListEqual(log, expected)
	# def test_info_1(self)

	def test_info_2(self):
		self.pLogger.setLevel(logging.WARNING)
		self.pLogger.info('Hello, World!')
		log = self.processTestLoggerLog()
		expected = []
		self.assertListEqual(log, expected)
	# def test_info_2(self)

	def test_removeHandler(self):
		# there always is one handler in this unittest
		self.assertEqual(len(self.pLogger.getHandlers()), 1)

		self.pLogger.removeHandler(self.pFileHandler)
		self.assertEqual(len(self.pLogger.getHandlers()), 0)

		self.pLogger.addHandler(self.pFileHandler)
		self.assertEqual(len(self.pLogger.getHandlers()), 1)
	# def test_removeHandler(self)

	def test_setLevel(self):
		self.pLogger.setLevel(logging.DEBUG)
		self.pLogger.warning('Hello, World!')
		self.pLogger.setLevel(logging.CRITICAL)
		self.pLogger.warning('Hello, World!')

		log = self.processTestLoggerLog()
		expected = ['Hello, World!']
		self.assertListEqual(log, expected)
	# def test_setLevel(self)

	def test_warning_1(self):
		self.pLogger.setLevel(logging.WARNING)
		self.pLogger.warning('Hello, World!')
		log = self.processTestLoggerLog()
		expected = ['Hello, World!']
		self.assertListEqual(log, expected)
	# def test_warning_1(self)

	def test_warning_2(self):
		self.pLogger.setLevel(logging.ERROR)
		self.pLogger.warning('Hello, World!')
		log = self.processTestLoggerLog()
		expected = []
		self.assertListEqual(log, expected)
	# def test_warning_2(self)
# class TestLogger(unittest.TestCase)