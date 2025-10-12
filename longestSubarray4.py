# https://leetcode.com/problems/longest-fibonacci-subarray/

class Solution(object):
	def longestSubarray(self, nums):
		l = 0
		res = 0
		for i in range(len(nums)):
			if i - 1 < 0 or i - 2 < 0:
				l += 1 
			elif nums[i] == nums[i - 1] + nums[i - 2]:
				l = max(l + 1, 3)
			else:
				l = 1

			res = max(res, l)

		return res