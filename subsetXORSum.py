# https://leetcode.com/problems/sum-of-all-subset-xor-totals/ 

class Solution(object):
	def subsetXORSum(self, nums):
		def allxors(i, sub):
			if i >= len(nums):
				return sub
			else:
				return allxors(i + 1, sub) + allxors(i + 1, sub ^ nums[i])
		return allxors(0, 0)
