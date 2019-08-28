# https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
	def longestCommonSubsequence(self, text1, text2):
		M = len(text1)
		N = len(text2)
		longest = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
		for i in range(1, M + 1):
			for j in range(1, N + 1):
				if text1[i - 1] == text2[j - 1]:
					longest[i][j] = longest[i - 1][j - 1] + 1
				else:
					longest[i][j] = max(longest[i - 1][j], longest[i][j - 1])
		return longest[M][N]
