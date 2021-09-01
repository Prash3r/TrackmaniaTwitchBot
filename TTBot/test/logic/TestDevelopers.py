# pylib
import unittest

# local
from TTBot.logic.Developers import Developers

class TestDevelopers(unittest.TestCase):
	def test_getMainDevelopers(self):
		pDevelopers = Developers()
		mainDevelopers = pDevelopers.getMainDevelopers()
		for mainDev in mainDevelopers:
			self.assertEqual(mainDevelopers.count(mainDev), 1)
			self.assertEqual(mainDev.lower(), mainDev)
		# for mainDev in mainDevelopers
	# def test_getMainDevelopers(self)

	def test_getModuleDevelopers(self):
		pDevelopers = Developers()
		moduleDevelopers = pDevelopers.getModuleDevelopers()
		for moduleDev in moduleDevelopers:
			self.assertEqual(moduleDevelopers.count(moduleDev), 1)
			self.assertEqual(moduleDev.lower(), moduleDev)
		# for moduleDev in moduleDevelopers
	# def test_getModuleDevelopers(self)

	def test__distinct(self):
		pDevelopers = Developers()
		mainDevelopers = pDevelopers.getMainDevelopers()
		moduleDevelopers = pDevelopers.getModuleDevelopers()

		for mainDev in mainDevelopers:
			self.assertNotIn(mainDev, moduleDevelopers)
		
		for moduleDev in moduleDevelopers:
			self.assertNotIn(moduleDev, mainDevelopers)
	# def test__distinct(self)
# class TestDevelopers(unittest.TestCase)