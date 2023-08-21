# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/ 

class Solution(object):
	def canMakeSubsequence(self, str1, str2):
		alpha = string.ascii_lowercase
		inc = {c: alpha[(i + 1) % len(alpha)] for i, c in enumerate(alpha)}

		i = 0
		j = 0
		while i < len(str1) and j < len(str2):
			if str1[i] == str2[j] or inc[str1[i]] == str2[j]:
				j += 1
			i += 1

		return j >= len(str2)
