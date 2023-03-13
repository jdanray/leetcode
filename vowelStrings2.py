# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution(object):
	def vowelStrings(self, words, left, right):
		vowels = "aeiou"

		res = 0
		for i in range(left, right + 1):
			if words[i][0] in vowels and words[i][-1] in vowels:
				res += 1

		return res
