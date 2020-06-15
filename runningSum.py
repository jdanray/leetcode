# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
	def runningSum(self, nums):
		s = 0
		res = []
		for n in nums:
			s += n
			res.append(s)
		return res
