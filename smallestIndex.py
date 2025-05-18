# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution(object):
	def smallestIndex(self, nums):
		for i, n in enumerate(nums):
			s = 0
			while n > 0:
				s += n % 10
				n //= 10

			if s == i:
				return i

		return -1