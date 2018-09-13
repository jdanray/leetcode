# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution(object):
	def frequencySort(self, s):
		f = {}
		for c in s:
			if c not in f:
				f[c] = 0
			f[c] += 1

		r = ''
		for c in sorted(f, key=lambda c: f[c], reverse=True):
			r += c * f[c]

		return r
