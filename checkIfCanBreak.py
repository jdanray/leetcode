# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution(object):
	def checkIfCanBreak(self, s1, s2):
		N = len(s1)

		def canBreak(x, y):
			x = sorted(x)
			y = sorted(y)
			return all(y[i] >= x[i] for i in range(N))

		return canBreak(s1, s2) or canBreak(s2, s1)
