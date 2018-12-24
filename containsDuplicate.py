# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
	def containsDuplicate(self, nums):
		return len(set(nums)) != len(nums)
