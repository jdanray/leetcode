# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution(object):
	def countGoodStrings(self, low, high, zero, one):
		MOD = 10**9 + 7

		memo = {}
		def dp(l):
			if l > high:
				return 0

			if l in memo:
				return memo[l]

			if l >= low:
				memo[l] = 1 + dp(l + zero) + dp(l + one)
			else:
				memo[l] = dp(l + zero) + dp(l + one)

			memo[l] %= MOD
			return memo[l]

		return dp(0)
