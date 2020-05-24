# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/ 

class Solution(object):
	def maxVowels(self, s, k):
		vowelset = {'a', 'e', 'i', 'o', 'u'}

		v = 0
		m = 0
		for i in range(len(s)):
			if s[i] in vowelset:
				v += 1

			if i - k >= 0 and s[i - k] in vowelset:
				v -= 1

			m = max(m, v)

		return m
