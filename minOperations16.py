# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

class Solution(object):
	def minOperations(self, nums, k):
		return -1 if any(n < k for n in nums) else len(set(nums) - {k})