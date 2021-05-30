# https://leetcode.com/problems/maximum-value-after-insertion/ 

class Solution(object):
	def maxValue(self, n, x):
		N = len(n)

		if n[0] == '-':
			i = 1
			cmp = lambda a, b: a <= b
		else:
			i = 0
			cmp = lambda a, b: a >= b

		while i < N and cmp(int(n[i]), x):
			i += 1

		return n[:i] + str(x) + n[i:]
