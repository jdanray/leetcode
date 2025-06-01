# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

class Solution(object):
	def checkEqualPartitions(self, nums, target):
		def canPart(i, a, b):
			if i >= len(nums):
				return a == target and b == target
			else:
				return canPart(i + 1, a * nums[i], b) or canPart(i + 1, a, b * nums[i])

		return canPart(0, 1, 1)