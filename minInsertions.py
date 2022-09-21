# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution(object):
	def minInsertions(self, s):
		memo = {}
		def dp(i, j):
			if i >= j:
				return 0

			if (i, j) in memo:
				return memo[i, j]

			if s[i] == s[j]:
				memo[i, j] = dp(i + 1, j - 1)
			else:
				memo[i, j] = 1 + min(dp(i + 1, j), dp(i, j - 1))
			return memo[i, j]

		return dp(0, len(s) - 1)
