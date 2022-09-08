# https://leetcode.com/problems/numbers-with-same-consecutive-differences/ 

class Solution(object):
	def numsSameConsecDiff(self, n, k):
		def generate(num, digs):
			if digs == 0:
				return [num]

			res = []
			d = num % 10
			if d + k <= 9:
				res += generate(num * 10 + (d + k), digs - 1)
			if k > 0 and d - k >= 0:
				res += generate(num * 10 + (d - k), digs - 1)

			return res

		res = []
		for num in range(1, 10):
			res += generate(num, n - 1)

		return res
