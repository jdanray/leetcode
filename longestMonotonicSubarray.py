# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/ 

class Solution(object):
	def longestMonotonicSubarray(self, nums):
		inc = 0
		dec = 0
		res = 0
		for i in range(len(nums)):
			if i > 0 and nums[i] > nums[i - 1]:
				inc += 1
			else:
				inc = 1

			if i > 0 and nums[i] < nums[i - 1]:
				dec += 1
			else:
				dec = 1

			res = max(res, inc, dec)

		return res
