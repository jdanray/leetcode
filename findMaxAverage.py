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

class Solution(object):
	def findMaxAverage(self, nums, k):
		i = 0
		s = 0.0
		res = float('-inf')
		for j, n in enumerate(nums):
			s += n

			if j >= k:
				s -= nums[i]
				i += 1

			if j - i + 1 == k:
				res = max(res, s)

		return res / k
