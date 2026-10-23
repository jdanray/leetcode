# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution(object):
	def countSubarrays(self, nums):
		return sum(nums[i] == 2 * (nums[i - 1] + nums[i + 1]) for i in range(1, len(nums) - 1))