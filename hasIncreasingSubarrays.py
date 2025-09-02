# https://leetcode.com/problems/prime-subtraction-operation/

class Solution(object):
	def hasIncreasingSubarrays(self, nums, k):
		inc = [1 for _ in range(len(nums))]
		for i, n in enumerate(nums):
			if i - 1 >= 0 and n > nums[i - 1]:
				inc[i] = inc[i - 1] + 1

			if inc[i] >= k and inc[i - k] >= k:
				return True

		return False