# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution(object):
	def maximumSubarraySum(self, nums, k):
		count = collections.Counter()
		i = 0
		s = 0
		res = 0
		for j, n in enumerate(nums):
			s += n
			count[n] += 1

			while j - i + 1 > k or count[n] > 1:
				count[nums[i]] -= 1
				s -= nums[i]
				i += 1

			if j - i + 1 == k:
				res = max(res, s)

		return res
