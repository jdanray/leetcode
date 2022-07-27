# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

class Solution(object):
	def canChoose(self, groups, nums, i=0, j=0):
		if i >= len(groups):
			return True

		if j >= len(nums):
			return False

		k = 0
		l = j
		while k < len(groups[i]) and l < len(nums) and groups[i][k] == nums[l]:
			k += 1
			l += 1

		if k == len(groups[i]):
			return self.canChoose(groups, nums, i + 1, l)

		return self.canChoose(groups, nums, i, j + 1)
