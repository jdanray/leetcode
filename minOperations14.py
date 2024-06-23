# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/ 

class Solution(object):
	def minOperations(self, nums):
		flipped = False
		res = 0
		for n in nums:
			if (n == 0 and not flipped) or (n == 1 and flipped):
				flipped = not flipped
				res += 1
		return res
