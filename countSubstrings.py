# https://leetcode.com/problems/palindromic-substrings/

class Solution(object):
	def countSubstrings(self, s):
		count = 0
		isPal = [[False for _ in range(len(s))] for _ in range(len(s))]
		for i in range(len(s) - 1, -1, -1):
			for j in range(i, len(s)):
				if s[i] == s[j] and (j - i < 3 or isPal[i + 1][j - 1]):
					isPal[i][j] = True
					count += 1
		return count
