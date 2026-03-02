# https://leetcode.com/problems/trim-trailing-vowels/

class Solution(object):
	def trimTrailingVowels(self, s):
		vowels = "aeiou"

		i = len(s) - 1
		while s[i] in vowels:
			i -= 1

		return s[:i]

class Solution(object):
	def trimTrailingVowels(self, s):
		vowels = 'aeiou'

		for i in range(len(s) - 1, -1, -1):
			if s[i] not in vowels:
				return s[:i + 1]

		return ''