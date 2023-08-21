# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/ 

class Solution(object):
	def countPairs(self, nums, target):
		res = 0
		for i, n in enumerate(nums):
			for j in range(i + 1, len(nums)):
				if n + nums[j] < target:
					res += 1
		return res
