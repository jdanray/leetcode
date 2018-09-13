# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution:
	primes = [2, 3, 5, 7, 11, 13, 17, 19]

	def isprime(self, num):
		return num in self.primes

	def nbits(self, num):
		nbits = 0
		while num > 0:
			if num & 1 == 1:
				nbits += 1
			num >>= 1
		return nbits

	def countPrimeSetBits(self, L, R):
		return sum(1 for n in range(L, R + 1) if self.isprime(self.nbits(n)))
