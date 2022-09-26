# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/ 

class Solution(object):
	def longestSubarray(self, nums):
		m = max(nums)
		l = 0
		res = 0
		for n in nums:
			if n == m:
				l += 1
			else:
				l = 0

			res = max(res, l)

		return res	
