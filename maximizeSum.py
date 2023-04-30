# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/ 

class Solution(object):
	def maximizeSum(self, nums, k):
		return k * max(nums) + k * (k - 1) // 2

class Solution(object):
	def maximizeSum(self, nums, k):
		m = max(nums)
		res = 0
		for _ in range(k):
			res += m
			m += 1
		return res
