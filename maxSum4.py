# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution(object):
	def maxSum(self, nums):
		s = 0
		seen = set()
		for n in nums:
			if n not in seen and n > 0:
				s += n
				seen.add(n)

		return max(nums) if not seen else s