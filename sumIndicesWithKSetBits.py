# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/ 

class Solution(object):
	def sumIndicesWithKSetBits(self, nums, k):
		res = 0
		for idx, n in enumerate(nums):
			b = 0
			while idx > 0:
				if idx & 1 == 1:
					b += 1
				idx >>= 1

			if b == k:
				res += n

		return res
