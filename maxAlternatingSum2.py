# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution(object):
	def maxAlternatingSum(self, nums):
		nums = sorted([abs(n) for n in nums])
		i = 0
		j = len(nums) - 1
		res = 0
		while i <= j:
			res += nums[j] * nums[j]
			if j > i:
				res -= nums[i] * nums[i]

			i += 1
			j -= 1

		return res