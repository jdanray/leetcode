# https://leetcode.com/problems/sort-integers-by-binary-reflection/

class Solution(object):
	def sortByReflection(self, nums):
		def reflect(num):
			res = 0
			while num > 0:
				res <<= 1
				res += (num & 1)
				num >>= 1
			return res

		return sorted(nums, key=lambda n: (reflect(n), n))