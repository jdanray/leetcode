# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution(object):
	def minSteps(self, s, t):
		scount = collections.Counter(s)
		tcount = collections.Counter(t)
		res = 0
		for c in scount:
			d = scount[c] - tcount[c]
			if d > 0: res += d
		return res
