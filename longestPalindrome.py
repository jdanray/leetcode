# https://leetcode.com/problems/longest-palindromic-substring/

"""
1) s[i][i] is a palindrome
2) s[i][j] is a palindrome if 

	a) s[i] == s[j]
	b) s[i + 1][j - 1] is a palindrome or j - i == 1
"""

class Solution(object):
	def longestPalindrome(self, s):
		dp = [[False for _ in range(len(s))] for _ in range(len(s))]
		imax = 0
		jmax = 0
		for i in range(len(s) - 1, -1, -1):
			dp[i][i] = True
			for j in range(i + 1, len(s)):
				if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]):
					dp[i][j] = True
					if j - i > jmax - imax:
						imax = i
						jmax = j

		return s[imax:jmax + 1]
