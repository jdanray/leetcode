# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/ 

class Solution(object):
	def sumCounts(self, nums):
		N = len(nums)

		res = 0
		for i in range(N):
			seen = set()
			for j in range(i, N):
				seen.add(nums[j])
				res += len(seen) ** 2

		return res
