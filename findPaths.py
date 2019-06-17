# https://leetcode.com/problems/out-of-boundary-paths/

class Solution(object):
	def findPaths(self, m, n, N, i, j):
		dij = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		M = 10**9 + 7
        
		memo = {}
		def dp(i, j, N):
			if i < 0 or i >= m or j < 0 or j >= n:
				return 1

			if N == 0:
				return 0

			if (i, j, N) in memo:
				return memo[i, j, N]	

			memo[i, j, N] = 0
			for di, dj in dij:
				memo[i, j, N] += dp(i + di, j + dj, N - 1) % M
				memo[i, j, N] %= M
                
			return memo[i, j, N]

		return dp(i, j, N)
