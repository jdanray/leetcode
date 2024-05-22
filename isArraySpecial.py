# https://leetcode.com/problems/special-array-i/ 

class Solution(object):
	def isArraySpecial(self, nums):
		return all(nums[i] % 2 != nums[i - 1] % 2 for i in range(1, len(nums)))
