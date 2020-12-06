# https://leetcode.com/problems/max-number-of-k-sum-pairs/ 

class Solution(object):
	def maxOperations(self, nums, k):
		nums = sorted(nums)
		res = 0
		i = 0
		j = len(nums) - 1
		while i < j:
			s = nums[i] + nums[j]
			if s > k:
				j -= 1
			elif s < k:
				i += 1
			else:
				res += 1
				i += 1
				j -= 1

		return res
