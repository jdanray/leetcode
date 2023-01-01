# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/ 

class Solution(object):
	def distinctPrimeFactors(self, nums):
		primes = set()
		for n in nums:
			# Factorize n
			# Algorithm credit: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

			while n % 2 == 0:
				primes.add(2)
				n //= 2

			d = 3
			while d <= math.sqrt(n):
				while n % d == 0:
					primes.add(d)
					n //= d
				d += 2

			if n > 2:
				primes.add(n)

		return len(primes)
