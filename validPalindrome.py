# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
	def isPalindrome(self, s, i, j):
		while i < j:
			if s[i] != s[j]:
				return False
			i += 1
			j -= 1
		return True

	def validPalindrome(self, s):
		i = 0
		j = len(s) - 1
		while i < j:
			if s[i] != s[j]:
				return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j - 1)
			i += 1
			j -= 1
		return True
