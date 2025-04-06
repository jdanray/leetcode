# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution(object):
	def minimumPairRemoval(self, nums):
		nondec = True
		minSum = [float('inf'), -1]
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				nondec = False

			s = nums[i] + nums[i + 1]
			if s < minSum[0]:
				minSum = [s, i]

		if nondec:
			return 0

		m = minSum[1]
		return 1 + self.minimumPairRemoval(nums[:m] + [nums[m] + nums[m + 1]] + nums[m + 2:])