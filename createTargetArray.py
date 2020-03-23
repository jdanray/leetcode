# https://leetcode.com/problems/create-target-array-in-the-given-order/ 

class Solution(object):
	def createTargetArray(self, nums, index):
		target = []
		for i, idx in enumerate(index):
			target = target[:idx] + [nums[i]] + target[idx:]
		return target
