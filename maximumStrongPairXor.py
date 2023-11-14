# https://leetcode.com/problems/maximum-strong-pair-xor-i/ 

class Solution(object):
	def maximumStrongPairXor(self, nums):
		m = 0
		for x in nums:
			for y in nums:
				if abs(x - y) <= min(x, y) and x ^ y > m:
					m = x ^ y
		return m
