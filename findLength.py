# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution(object):
	def findLength(self, A, B):
		M = 0
		memo = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
		for i in range(len(A) - 1, -1, -1):
			for j in range(len(B) - 1, -1, -1):
				if A[i] == B[j]:
					memo[i][j] = 1 + memo[i + 1][j + 1]
					M = max(M, memo[i][j]) 
		return M



