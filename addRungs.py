# https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution(object):
	def addRungs(self, rungs, dist):
		res = 0
		height = 0
		for r in rungs:
			res += (r - height - 1) // dist
			height = r
		return res
