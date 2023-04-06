# https://leetcode.com/problems/maximum-xor-after-operations/ 

class Solution(object):
	def maximumXOR(self, nums):
		return reduce(lambda x, y: x | y, nums)
