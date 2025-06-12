# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution(object):
	def maxAdjacentDistance(self, nums):
		return max(abs(nums[i] - nums[(i + 1) % len(nums)]) for i in range(len(nums)))