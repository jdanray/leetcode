# https://leetcode.com/problems/maximum-erasure-value/

class Solution(object):
	def maximumUniqueSubarray(self, nums):
		i = 0
		res = 0
		s = 0
		seen = collections.defaultdict(bool)
		for j, n in enumerate(nums):
			while seen[n]:
				seen[nums[i]] = False
				s -= nums[i]
				i += 1

			s += nums[j]
			seen[nums[j]] = True

			res = max(res, s)

		return res
