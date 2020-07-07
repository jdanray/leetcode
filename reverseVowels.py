# https://leetcode.com/problems/reverse-vowels-of-a-string/ 

class Solution(object):
	def reverseVowels(self, s):
		allvowels = "aeiouAEIOU"
		vowel = [c for c in s if c in allvowels]
		v = len(vowel) - 1
		res = ""
		for c in s:
			if c in allvowels:
				res += vowel[v]
				v -= 1
			else:
				res += c

		return res	
