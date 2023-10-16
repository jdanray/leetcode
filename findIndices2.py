# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/ 

class Solution(object):
	def findIndices(self, nums, idxDif, valDif):
		minim = [float('inf'), -1]
		maxim = [float('-inf'), -1]
		for i, n in enumerate(nums):
			j = i - idxDif

			if j >= 0 and nums[j] < minim[0]:
				minim = [nums[j], j]
			if j >= 0 and nums[j] > maxim[0]:
				maxim = [nums[j], j]

			if maxim[0] - n >= valDif:
				return [maxim[1], i]
			if n - minim[0] >= valDif:
				return [minim[1], i]

		return [-1, -1]
