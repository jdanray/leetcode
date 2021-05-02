# https://leetcode.com/problems/minimum-distance-to-the-target-element/ 

class Solution(object):
	def getMinDistance(self, nums, target, start):
		res = float('inf')
		for i, n in enumerate(nums):
			if n == target:
				res = min(res, abs(i - start))
		return res
