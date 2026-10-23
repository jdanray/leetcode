# https://leetcode.com/problems/maximum-points-tourist-can-earn/submissions/

# Py3
class Solution(object):
	def maxScore(self, n, k, stayScore, travelScore):
		@functools.lru_cache(None)
		def dp(cur, i):
			if i == k:
				return 0

			res = dp(cur, i + 1) + stayScore[i][cur]
			for dest in range(n):
				if dest != cur:
					res = max(res, dp(dest, i + 1) + travelScore[cur][dest])

			return res

		return max(dp(cur, 0) for cur in range(n))