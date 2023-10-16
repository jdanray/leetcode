# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/ 

class Solution(object):
	def numWays(self, steps, arrLen):
		MOD = 10**9 + 7

		memo = {}
		def dp(i, steps):
			if steps == 0 and i == 0:
				return 1

			if i < 0 or i >= arrLen or i > steps:
				return 0

			if (i, steps) in memo:
				return memo[i, steps]

			stay = dp(i, steps - 1)
			right = dp(i + 1, steps - 1)
			left = dp(i - 1, steps - 1)

			memo[i, steps] = (stay + right + left) % MOD
			return memo[i, steps]

		return dp(0, steps)
