# https://leetcode.com/problems/count-vowel-substrings-of-a-string/ 

class Solution(object):
	def countVowelSubstrings(self, word):
		vowels = "aeiou"
		N = len(word)

		res = 0
		for i in range(N):
			seen = set()
			j = i
			while j < N and word[j] in vowels:
				seen.add(word[j])				
				if len(seen) == len(vowels):
					res += 1
				j += 1

		return res
