# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/ 

class Solution(object):
	def minOperations(self, nums, numsDivide):
		g = numsDivide[0]
		for n in numsDivide[1:]:
			while n != 0:
				g, n = n, g % n

		nums = sorted(nums)
		for i, n in enumerate(nums):
			if g % n == 0:
				return i

		return -1
