# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/ 

class Solution(object):
	def maxSubarrayLength(self, nums, k):
		count = collections.Counter()
		i = 0
		res = 0
		for j, n in enumerate(nums):
			count[n] += 1

			while count[n] > k:
				count[nums[i]] -= 1
				i += 1

			res = max(res, j - i + 1)

		return res
