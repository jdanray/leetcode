# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
	def findMaxConsecutiveOnes(self, nums):
		c = 0
		m = 0
		for n in nums:
			if n == 1:
				c += 1
			else:
				c = 0
			if c > m:
				m = c
		return m
