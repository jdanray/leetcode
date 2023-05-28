class Solution(object):
	def stoneGameVII(self, stones):
		N = len(stones)

		remain = [[0 for _ in range(N)] for _ in range(N)]
		for i in range(N):
			s = 0
			for j in range(i, N):
				s += stones[j]
				remain[i][j] = s

		@functools.lru_cache(None)
		def dp(i, j):
			if i > j:
				return 0

			left = remain[i + 1][j] if i + 1 < N else 0
			right = remain[i][j - 1] if j - 1 >= 0 else 0

			return max(left - dp(i + 1, j), right - dp(i, j - 1))

		return dp(0, N - 1)
