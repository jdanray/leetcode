# https://leetcode.com/problems/majority-element/description/

class Solution(object):
	def majorityElement(self, nums):
		s = 0
		for k in nums:
			if s == 0:
				p = k
			if k == p:
				s += 1
			else:
				s -= 1
		return p
