# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution(object):
	def countDigits(self, num):
		n = num
		res = 0
		while n > 0:
			d = n % 10
			if num % d == 0:
				res += 1
			n //= 10
		return res
