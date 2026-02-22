# https://leetcode.com/problems/check-digitorial-permutation/

class Solution(object):
	def isDigitorialPermutation(self, n):
		def sfd(n):
			s = 0
			while n > 0:
				s += math.factorial(n % 10)
				n //= 10
			return s

		def count(n):
			c = collections.Counter()
			while n > 0:
				c[n % 10] += 1
				n //= 10
			return c

		return count(n) == count(sfd(n))