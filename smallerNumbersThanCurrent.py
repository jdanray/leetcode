# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/ 

class Solution(object):
	def smallerNumbersThanCurrent(self, nums):
		res = []
		for i, m in enumerate(nums):
			res.append(0)
			for j, n in enumerate(nums):
				if i != j and n < m:
					res[-1] += 1
		return res
