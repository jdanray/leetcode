# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/ 

class Solution(object):
	def minChanges(self, n, k):
		res = 0
		while n > 0 or k > 0:
			a = n & 1
			b = k & 1

			if a == 0 and b == 1:
				return -1

			if a == 1 and b == 0:
				res += 1

			n >>= 1
			k >>= 1

		return res
