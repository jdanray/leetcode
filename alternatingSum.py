# https://leetcode.com/problems/compute-alternating-sum/

class Solution(object):
	def alternatingSum(self, nums):
		return sum(n if i % 2 == 0 else -n for i, n in enumerate(nums))