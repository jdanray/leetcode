# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
	def findMaxAverage(self, nums, k):
		s = sum(nums[i] for i in range(k))
		M = s
		for i in range(k, len(nums)):
			s -= nums[i - k]
			s += nums[i]
			M = max(M, s)
		return M / k
