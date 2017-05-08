import unittest

from prime_numbers import primes

class primes(unittest.TestCase):

	def test_it_flags_negative_input(self):
		self.assertEqual(primes(-10), "Negative input")

		
if __name__ == '__main__':
	unittest.main()

