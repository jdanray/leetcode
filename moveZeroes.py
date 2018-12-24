# https://leetcode.com/problems/move-zeroes/description/

class Solution:
	def moveZeroes(self, nums):
		i = 0
		z = 0
		while i < len(nums) - z:
			if nums[i] != 0:
				i += 1
				continue
			z += 1
			for j in range(i + 1, len(nums)):
				nums[j - 1] = nums[j]
			nums[-1] = 0
