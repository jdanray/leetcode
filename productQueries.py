# https://leetcode.com/problems/range-product-queries-of-powers/ 

class Solution(object):
	def productQueries(self, n, queries):
		MOD = 10**9 + 7

		powers = []
		p = 0
		while n > 0:
			if n & 1 == 1:
				powers.append(1 << p)
			p += 1
			n >>= 1

		res = []
		for (left, right) in queries:
			prod = 1
			for i in range(left, right + 1):
				prod *= powers[i]
			prod %= MOD
			res.append(prod)

		return res
