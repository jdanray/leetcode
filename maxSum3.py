# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/ 

class Solution(object):
	def maxSum(self, nums, m, k):
		count = collections.Counter()
		ndistinct = 0
		s = 0
		res = 0
		for i, n in enumerate(nums):
			s += n
			count[n] += 1

			if count[n] == 1:
				ndistinct += 1

			if i >= k:
				s -= nums[i - k]
				count[nums[i - k]] -= 1
				if count[nums[i - k]] == 0:
					ndistinct -= 1

			if ndistinct >= m:
				res = max(res, s)

		return res
