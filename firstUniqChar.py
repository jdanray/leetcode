# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution(object):
	def firstUniqChar(self, s):
		f = {}
		for c in s:
			if c not in f:
				f[c] = 0
			f[c] += 1

		for i, c in enumerate(s):
			if f[c] == 1:
				return i

		return -1
