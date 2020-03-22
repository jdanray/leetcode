# https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution(object):
	def getKth(self, lo, hi, k):
		def power(num):
			p = 0
			while num != 1:
				if num % 2 == 0:
					num //= 2
				else:
					num = 3 * num + 1
				p += 1
			return p

		sortval = sorted(range(lo, hi + 1), key=power)
		return sortval[k - 1]
