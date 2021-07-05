# https://leetcode.com/problems/build-array-from-permutation/

class Solution(object):
	def buildArray(self, nums):
		return [nums[n] for n in nums]
