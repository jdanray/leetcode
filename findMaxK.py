# https://leetcode.comproblems/largest-positive-integer-that-exists-with-its-negative/

class Solution(object):
	def findMaxK(self, nums):
		nums = set(nums)
		res = -1
		for n in nums:
			if -n in nums:
				res = max(res, abs(n))

		return res
