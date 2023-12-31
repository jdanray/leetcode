# https://leetcode.com/problems/minimum-number-game/

class Solution(object):
	def numberGame(self, nums):
		nums = sorted(nums)
		return [nums[i + 1] if i % 2 == 0 else nums[i - 1] for i in range(len(nums))]
