# https://leetcode.com/problems/sort-the-jumbled-numbers/ 

class Solution(object):
	def sortJumbled(self, mapping, nums):
		def convert(num):
			if num == 0:
				return mapping[0]

			res = 0
			place = 1
			while num > 0:
				d = num % 10
				res += place * mapping[d]
				place *= 10
				num //= 10
			return res

		res = sorted((convert(n), i) for i, n in enumerate(nums))
		return [nums[r[1]] for r in res]
