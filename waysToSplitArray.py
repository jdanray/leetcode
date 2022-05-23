# https://leetcode.com/problems/number-of-ways-to-split-array/  

class Solution(object):
	def waysToSplitArray(self, nums):
		left = 0
		right = sum(nums)
		res = 0
		for n in nums[:-1]:
			left += n
			right -= n

			if left >= right:
				res += 1

		return res
