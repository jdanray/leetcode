# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/ 

class Solution(object):
	def countHillValley(self, nums):
		res = 0
		pre = nums[0]
		for i in range(1, len(nums) - 1):
			if (nums[i] > pre and nums[i] > nums[i + 1]) or (nums[i] < pre and nums[i] < nums[i + 1]):
				res += 1
				pre = nums[i]
		return res
