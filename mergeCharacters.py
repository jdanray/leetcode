# https://leetcode.com/problems/merge-close-characters/

class Solution(object):
	def mergeCharacters(self, s, k):
		idx = {}
		i = 0
		res = ''
		for c in s:
			if c in idx and i - idx[c] <= k:
				i -= 1
			else:
				idx[c] = i
				res += c
			i += 1

		return res