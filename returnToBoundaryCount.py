# https://leetcode.com/problems/ant-on-the-boundary/ 

class Solution(object):
	def returnToBoundaryCount(self, nums):
		res = 0
		loc = 0
		for n in nums:
			loc += n
			if loc == 0:
				res += 1
		return res
