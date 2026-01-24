# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

"""
Initially, we haven't selected/paired any numbers. Now, let nums[j] be the largest number that we haven't selected yet. If nums[j] is a part of the minimized maximum pair (nums[i], nums[j]), then nums[i] must be the smallest available number; otherwise, nums[i] + nums[j] won't be minimal. Therefore, the largest unpaired number must always be paired with the smallest unpaired number.
"""

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
