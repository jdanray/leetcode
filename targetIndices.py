# https://leetcode.com/problems/find-target-indices-after-sorting-array/ 

class Solution(object):
	def targetIndices(self, nums, target):
		return [i for i, n in enumerate(sorted(nums)) if n == target]
