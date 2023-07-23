# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution(object):
	def sortVowels(self, s):
		vowels = 'AEIOUaeiou'

		count = collections.Counter()
		for c in s:
			if c in vowels:
				count[c] += 1

		i = 0
		res = ''
		for c in s:
			if c not in vowels:
				res += c
				continue

			while count[vowels[i]] < 1:
				i += 1

			res += vowels[i]
			count[vowels[i]] -= 1

		return res
