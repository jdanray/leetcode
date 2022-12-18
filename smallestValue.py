# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/ 

class Solution(object):
	def smallestValue(self, n):
		def sumFactors(n):
			res = 0
			while n % 2 == 0:
				res += 2
				n //= 2

			i = 3
			rt = n ** 0.5
			while i <= rt:
				while n % i == 0:
					res += i
					n //= i
				i += 2

			if n > 1:
				res += n

			return res

		s = sumFactors(n)
		while n != s:
			n = s
			s = sumFactors(n)

		return s
