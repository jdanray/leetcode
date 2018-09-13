# https://leetcode.com/problems/subsets/description/

class Solution(object):
	def subsets(self, nums):
		p = [[]]
		for x in nums:
			p += [y + [x] for y in p]
		return p
