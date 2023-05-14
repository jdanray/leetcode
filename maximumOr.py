# https://leetcode.com/problems/maximum-or/ 

class Solution(object):
	def maximumOr(self, nums, k):
		N = len(nums)

		right = [0 for _ in range(N)]
		for i in range(N - 2, -1, -1):
			right[i] = nums[i + 1] | right[i + 1]

		left = 0
		res = 0
		for i, n in enumerate(nums):
			res = max(res, left | (n << k) | right[i])
			left |= n

		return res
