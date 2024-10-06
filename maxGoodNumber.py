# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution(object):
	def maxGoodNumber(self, nums):
		def concat(nums):
			res = 0
			for n in nums:               
				oldn = n
				l = 0
				while n > 0:
					l += 1
					n >>= 1

				for i in range(l):
					res <<= 1
					if (oldn >> (l - i - 1)) & 1 == 1:
						res += 1

			return res

		return max(concat(p) for p in itertools.permutations(nums))
