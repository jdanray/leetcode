# https://leetcode.com/problems/vowels-of-all-substrings/

class Solution(object):
	def countVowels(self, word):
		vowels = "aeiou"

		nvows = 0
		res = 0
		for i, c in enumerate(word):
			if c in vowels:
				nvows += (i + 1)
                
			res += nvows

		return res
