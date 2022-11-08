# https://leetcode.com/problems/apply-operations-to-an-array/ 

class Solution(object):
	def applyOperations(self, nums):
		N = len(nums)
		for i in range(N - 1):
			if nums[i] == nums[i + 1]:
				nums[i] *= 2
				nums[i + 1] = 0

		nonzeros = [n for n in nums if n != 0]
		zeros = [n for n in nums if n == 0]

		return nonzeros + zeros
