# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution(object):
	def minPairSum(self, nums):
		nums = sorted(nums)
		i = 0
		j = len(nums) - 1
		res = 0
		while i < j:
			res = max(res, nums[i] + nums[j])
			i += 1
			j -= 1

		return res
