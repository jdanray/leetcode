# https://leetcode.com/problems/count-good-numbers/ 

class Solution(object):
	def countGoodNumbers(self, n):
		MOD = 10**9 + 7
		E = 5
		O = 4

		def power(x, y):
			x %= MOD
			if x == 0:
				return 0

			res = 1
			while y > 0:
				if y & 1 == 1:
					res = (res * x) % MOD
				y >>= 1
				x = (x * x) % MOD

			return res

		p = n // 2
		return (power(E, n - p) * power(O, p)) % MOD
