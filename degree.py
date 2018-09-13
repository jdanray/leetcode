# https://leetcode.com/problems/degree-of-an-array/description/

class Solution:
	def findShortestSubArray(self, nums):
		d = 0
		l = 0
		f = dict()
		for i, n in enumerate(nums):
			if n not in f:
				f[n] = []
			f[n].append(i)
			if len(f[n]) > d:
				d = len(f[n])
				l = f[n][-1] - f[n][0] + 1
			elif len(f[n]) == d:
				l = min(l, f[n][-1] - f[n][0] + 1)
		return l
