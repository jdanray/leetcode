# https://leetcode.com/problems/count-vowel-strings-in-ranges/ 

class Solution(object):
	def vowelStrings(self, words, queries):
		vowels = set('aeiou')

		count = [0 for _ in range(len(words) + 1)]
		for i, w in enumerate(words):
			count[i + 1] = count[i]
			if w[0] in vowels and w[-1] in vowels:
				count[i + 1] += 1

		res = []
		for (l, r) in queries:
			c = count[r + 1] - count[l]
			res.append(c)

		return res
