# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/ 

class Solution(object):
	def sortByBits(self, arr):
		def numBits(n):
			res = 0
			while n > 0:
				res += (n & 1)
				n >>= 1
			return res

		return sorted(arr, key=lambda a: (numBits(a), a))
