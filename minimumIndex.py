# https://leetcode.com/problems/minimum-index-of-a-valid-split/ 

class Solution(object):
	def majorityElement(self, nums):
		c = 0
		p = -1
		for n in nums:
			if c == 0:
				p = n

			if n == p:
				c += 1
			else:
				c -= 1

		return p

	def minimumIndex(self, nums):
		d = self.majorityElement(nums)
		f = len([n for n in nums if n == d])
		c = 0
		for i, n in enumerate(nums):
			if n == d:
				c += 1

			if c * 2 > (i + 1) and (f - c) * 2 > (len(nums) - i - 1):
				return i

		return -1
