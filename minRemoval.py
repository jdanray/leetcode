# https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution(object):
	def minRemoval(self, nums, k):
		N = len(nums)

		nums = sorted(nums)
		res = N - 1
		for i, n in enumerate(nums):
			j = bisect.bisect(nums, n * k)
			if nums[j - 1] <= n * k:
				res = min(res, i + N - j)

		return res