# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

class Solution(object):
	def minBitwiseArray(self, nums):
		res = []
		for n in nums:
			res.append(-1)
			for cand in range(2, n + 1):
				if cand | (cand + 1) == n:
					res[-1] = cand
					break

		return res