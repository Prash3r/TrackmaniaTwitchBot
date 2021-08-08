# pylib
import unittest

# local
from TTBot.logic.Randomizer import Randomizer

class TestRandomizer(unittest.TestCase):
	def test_uniformFloat(self):
		pRandomizer = Randomizer()

		for _ in range(1000):
			f = pRandomizer.uniformFloat(2.7818, 3.1416)
			self.assertTrue(2.7818 <= f <= 3.1416)
		# for _ in range(1000)
	# def test_uniformFloat(self)

	def test_uniformInt(self):
		pRandomizer = Randomizer()

		for _ in range(1000):
			i = pRandomizer.uniformInt(5, 20)
			self.assertTrue(5 <= i <= 20)
		# for _ in range(1000)
	# def test_uniformInt(self)
# class TestRandomizer(unittest.TestCase)