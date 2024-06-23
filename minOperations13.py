# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/ 

class Solution(object):
	def minOperations(self, nums):
		ops = 0
		for i in range(len(nums) - 2):
			if nums[i] == 0:
				nums[i] = 1
				nums[i + 1] = 1 - nums[i + 1]
				nums[i + 2] = 1 - nums[i + 2]
				ops += 1

		return ops if all(n == 1 for n in nums) else -1
