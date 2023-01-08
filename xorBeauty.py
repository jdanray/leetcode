# https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution(object):
	def xorBeauty(self, nums):
		res = 0
		for n in nums:
			res ^= n           
		return res
