# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/ 

class Solution(object):
	def sumOfEncryptedInt(self, nums):
		def encrypt(num):
			m = 0
			l = 0
			while num > 0:
				d = num % 10
				m = max(m, d)
				l += 1
				num //= 10

			res = 0
			for _ in range(l):
				res *= 10
				res += m

			return res

		return sum(encrypt(n) for n in nums)
