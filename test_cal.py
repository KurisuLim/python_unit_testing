import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add(self):
		result = calc.add(10,5)
		self.assertEqual(result, 15)
		
		print("Test Success for Addition.")

	def test_sub(self):
		result = calc.subtract(10,5)
		self.assertEqual(result, 5)
		print("Test Success for Subtraction.")

	def test_mul(self):
		result = calc.multiply(5,5)
		self.assertEqual(result, 25)
		print("Test Success for Multiplication.")

	def test_div(self):
		result = calc.divide(10,5)
		self.assertEqual(result, 2)
		print("Test Success for Division.")

if __name__ == "__main__":
	unittest.main()