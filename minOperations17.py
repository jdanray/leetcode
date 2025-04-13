# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution(object):
	def minOperations(self, nums, k):
		s = sum(nums)
		res = 0
		while s % k != 0:
			s -= 1
			res += 1
		return res