# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution(object):
	def minOperations(self, nums, k):
		return sum(nums) % k
