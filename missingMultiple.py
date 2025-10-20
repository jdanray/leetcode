# https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution(object):
	def missingMultiple(self, nums, k):
		nums = set(nums)
		p = 1
		while k * p in nums:
			p += 1
		return k * p