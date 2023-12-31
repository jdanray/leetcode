# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/ 

class Solution(object):
	def minDifficulty(self, diff, d):
		if d > len(diff):
			return -1

		memo = {}
		def dp(i, d):
			if d == 1:
				return max(diff[i:])

			if (i, d) in memo:
				return memo[i, d]

			m = 0
			res = float('inf')
			for j in range(i, len(diff) - d + 1):
				m = max(m, diff[j])
				res = min(res, m + dp(j + 1, d - 1))

			memo[i, d] = res
			return memo[i, d]

		return dp(0, d)
