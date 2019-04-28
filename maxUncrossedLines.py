# https://leetcode.com/problems/uncrossed-lines/

class Solution(object):
	def maxUncrossedLines(self, A, B):
		memo = {}
		def dp(i, j):
			if i >= len(A) or j >= len(B):
				return 0

			if (i, j) in memo:
				return memo[(i, j)]

			memo[(i, j)] = dp(i + 1, j)
			for k in range(j, len(B)):
				if A[i] == B[k]:
					memo[(i, j)] = max(1 + dp(i + 1, k + 1), memo[(i, j)])
					return memo[(i, j)]

			return memo[(i, j)]

		return dp(0, 0)
