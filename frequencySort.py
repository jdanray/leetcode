# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution(object):
	def frequencySort(self, s):
		freq = {}
		for c in s:
			if c not in freq:
				freq[c] = 0
			freq[c] += 1

		res = ''
		sortchars = sorted(freq, key=lambda c: freq[c], reverse=True)
		for c in sortchars:
			res += (c * freq[c])
		return res
