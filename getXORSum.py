# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/ 

class Solution(object):
	def getXORSum(self, arr1, arr2):
		xor = 0
		for a in arr2:
			xor ^= a

		res = 0
		for a in arr1:
			res ^= (a & xor)

		return res
