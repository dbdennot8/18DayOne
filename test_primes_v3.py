import unittest

from prime_numbers import primes

class primes(unittest.TestCase):

	def test_it_flags_negative_input(self):
		self.assertEqual(primes(-10), "Negative input")

	def test_it_only_takes_integer_inputs(self):
		self.assertEqual(primes([1,2,3]), "Invalid input")

	def test_it_returns_a_list(self):
		self.assertTrue(primes(10), [2,3,5,7])

if __name__ == '__main__':
	unittest.main()

