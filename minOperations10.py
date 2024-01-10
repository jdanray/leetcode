# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/ 

class Solution(object):
	def minOperations(self, nums, k):
		res = 0
		for i in range(32):
			xor = 0
			for n in nums:
				xor ^= (n >> i) & 1

			if xor != (k >> i) & 1:
				res += 1

		return res
