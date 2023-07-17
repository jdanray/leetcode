# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution(object):
	def sumOfSquares(self, nums):
		return sum(n ** 2 for i, n in enumerate(nums) if len(nums) % (i + 1) == 0)
