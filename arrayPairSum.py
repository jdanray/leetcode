# https://leetcode.com/problems/array-partition-i/submissions/

class Solution(object):
	def arrayPairSum(self, nums):
		nums = sorted(nums)
		return sum(nums[i] for i in range(0, len(nums), 2))
