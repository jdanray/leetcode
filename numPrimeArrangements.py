# https://leetcode.com/problems/prime-arrangements/

class Solution(object):
	def numPrimeArrangements(self, n):
		isprime = {i: True for i in range(n + 1)}
		for i in range(2, int(math.sqrt(n)) + 1):
			if isprime[i]:
				j = 2
				while j * i <= n:
					isprime[j * i] = False
					j += 1

		MOD = 10**9+7
		k = len([i for i in isprime if isprime[i] and i >= 2])
		res = 1
		for i in range(1, k + 1):
			res *= i
			res %= MOD
		for i in range(1, n - k + 1):
			res *= i
			res %= MOD
            
		return res

import functools

class Solution(object):
	MOD = 10**9+7

	def genPrimes(self, n):
		isprime = {i: True for i in range(n + 1)}
		for i in range(2, int(math.sqrt(n)) + 1):
			if isprime[i]:
				j = 2
				while j * i <= n:
					isprime[j * i] = False
					j += 1
		return isprime

	def countPrimes(self, n):
		isprime = self.genPrimes(n)
		return len([i for i in isprime if isprime[i] and i >= 2])

	def reduce(self, n):
		return functools.reduce(lambda x, y: x * y, range(1, n + 1))

	def mul(self, n, k):
		return self.reduce(k) % self.MOD * self.reduce(n - k) % self.MOD 

	def numPrimeArrangements(self, n):
		return 1 if n == 1 else self.mul(n, self.countPrimes(n))

class Solution(object):
	def numPrimeArrangements(self, n):
		MOD = 10 ** 9 + 7

		# sieve of eratosthenes
		# compute all primes from 1 to n
		isprime = [True for _ in range(n + 1)]
		isprime[1] = False
		i = 2
		while i * i <= n:
			for j in range(2, n // i + 1):
				isprime[j * i] = False

			i += 1
			while not isprime[i]:
				i += 1

		# count the primes and composites
		c = 0
		p = 0
		for i in range(1, n + 1):
			if isprime[i]:
				p += 1
			else:
				c += 1

		# the number of valid arrangements is the factorial of c, times the factorial of p
		# for the first prime index, there are p primes we could assign to that index 
		# for the second prime index, there are (p - 1) primes available
		# etc, etc
		# the same goes for the composite indexes
		return (factorial(c) * factorial(p)) % MOD
