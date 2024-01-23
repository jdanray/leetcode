# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/ 

class Solution(object):
	def minimumPushes(self, word):
		K = 8
		m = {}
		res = 0
		for c in word:
			if c not in m:
				m[c] = len(m)

			res += (m[c] // K) + 1

		return res
