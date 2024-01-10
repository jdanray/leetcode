# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/ 

class Solution(object):
	def missingInteger(self, nums):
		s = nums[0]
		l = 1
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1] + 1:
				break

			l += 1
			s += nums[i]

		nums = set(nums)
		while s in nums:
			s += 1

		return s
