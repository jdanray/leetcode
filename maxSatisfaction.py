# https://leetcode.com/problems/reducing-dishes/ 

class Solution(object):
	def maxSatisfaction(self, s):
		s = sorted(s)

		memo = {}
		def dp(i, t):
			if i >= len(s):
				return 0 

			if (i, t) not in memo:
				incl = dp(i + 1, t + 1) + (s[i] * t)
				excl = dp(i + 1, t)
				memo[i, t] = max(incl, excl)
			return memo[i, t]

		return dp(0, 1)
