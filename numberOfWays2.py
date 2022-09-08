# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution(object):
	def numberOfWays(self, startPos, endPos, k):
		MOD = 10**9 + 7

		memo = {}
		def dp(pos, k):
			if k == 0:
				return pos == endPos

			if (pos, k) not in memo:
				memo[pos, k] = (dp(pos - 1, k - 1) + dp(pos + 1, k - 1)) % MOD

			return memo[pos, k]

		return dp(startPos, k)
