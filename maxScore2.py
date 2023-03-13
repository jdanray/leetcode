# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/ 

class Solution(object):
	def maxScore(self, nums):
		nums = sorted(nums, reverse=True)
		res = 0
		pre = 0
		for n in nums:
			pre += n
			if pre > 0:
				res += 1

		return res
