# https://leetcode.com/problems/next-greater-element-i/description/

class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		res = []
		for f in findNums:
			i = 0
			while nums[i] != f:
				i += 1
			while i < len(nums) and nums[i] <= f:
				i += 1
			if i >= len(nums) or nums[i] <= f:
				res.append(-1)
			else:
				res.append(nums[i])
		return res
