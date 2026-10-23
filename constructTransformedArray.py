# https://leetcode.com/problems/transformed-array/

class Solution(object):
	def constructTransformedArray(self, nums):
		return [nums[(i + n) % len(nums)] for i, n in enumerate(nums)]