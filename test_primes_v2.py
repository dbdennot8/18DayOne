import unittest

from prime_numbers import primes

class primes(unittest.TestCase):

	def test_it_flags_negative_input(self):
		self.assertEqual(primes(-10), "Negative input")

	def test_it_only_takes_integer_inputs(self):
		self.assertEqual(primes([1,2,3]), "Invalid input")
		
if __name__ == '__main__':
	unittest.main()

