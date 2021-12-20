# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/ 

class Solution(object):
	def firstPalindrome(self, words):
		def isPal(word):
			i = 0
			j = len(word) - 1
			while i < j and word[i] == word[j]:
				i += 1
				j -= 1
			return i >= j

		for w in words:
			if isPal(w):
				return w

		return ""
