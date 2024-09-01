# https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution(object):
	def generateKey(self, num1, num2, num3):
		N = 4

		p = 1
		res = 0
		for _ in range(N):
			res += p * min(num1 % 10, num2 % 10, num3 % 10)

			p *= 10
			num1 //= 10
			num2 //= 10
			num3 //= 10

		return res
