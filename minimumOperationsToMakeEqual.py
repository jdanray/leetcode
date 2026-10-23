# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution(object):
	def minimumOperationsToMakeEqual(self, x, y):
		MULT = [5, 11]

		memo = {}
		def dp(x):
			if x <= y:
				return y - x

			if x in memo:
				return memo[x]

			res = x - y
			for m in MULT:
				d = x % m
				res = min(res, d + 1 + dp((x - d) // m))

				i = m - d
				res = min(res, i + 1 + dp((x + i) // m))

			memo[x] = res
			return memo[x]

		return dp(x)