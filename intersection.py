# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution(object):
	def intersection(self, nums):
		return sorted(set(nums[0]).intersection(*nums[1:]))
