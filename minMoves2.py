# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution(object):
	def minMoves(self, nums):
		m = max(nums)
		return sum(m - n for n in nums)