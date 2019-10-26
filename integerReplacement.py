# https://leetcode.com/problems/integer-replacement/ 

class Solution(object):
	def integerReplacement(self, n):
		memo = {}
		def helper(n):
			if n == 1:
				return 0
			elif n not in memo:
				if n % 2 == 0:
					memo[n] = 1 + helper(n // 2)
				else:
					memo[n] = 1 + min(helper(n + 1), helper(n - 1))
			return memo[n]

		return helper(n)
