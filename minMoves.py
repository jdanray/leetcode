# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/ 

class Solution(object):
	def minMoves(self, nums):
		nums = sorted(nums)
		mini = nums[0]
		d = 0
		for i in range(len(nums) - 1, 0, -1):
			nums[i] += d
			d += nums[i] - mini
			mini = nums[i]
		return d
