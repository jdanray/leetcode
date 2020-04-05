# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/ 

class Solution(object):
	def minSubsequence(self, nums):
		nums = sorted(nums, reverse=True)
		total = sum(nums)
		s = 0
		res = []
		for n in nums:
			res.append(n)
			s += n
			if s > total - s:
				return res
