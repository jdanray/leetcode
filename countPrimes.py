# https://leetcode.com/problems/count-primes/

class Solution:
	def countPrimes(self, n):
		if n < 2:
			return 0

		b = {i: True for i in range(2, n)}
		i = 2
		rt = n ** 0.5
		while i <= rt:
			for j in range(2, (n // i) + 1):
				b[j * i] = False

			i += 1
			while not b[i]:
				i += 1

		return len([k for k in b if b[k]])
