# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/ 

class Solution(object):
	def minOperations(self, nums, k):
		res = 0
		for n in nums:
			if n < k:
				res += 1
		return res
