def primes(n):
	list_of_primes = []

	if not isinstance(n, int):
		return "Invalid input"

	elif n == 0:
		return []

	elif n < 0:
		return "Sorry.Please enter a  positive number."

	else:
		for num in range(2,n+1):
			prime = True

			for i in range(2,num):
				if (num % i == 0):
					prime = False
			if prime:
				list_of_primes.append(num)

		return list_of_primes
"""
print primes(-7)
print primes(10)
print primes("dennis")
print primes(0)
"""