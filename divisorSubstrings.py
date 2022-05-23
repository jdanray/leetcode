# https://leetcode.com/problems/find-the-k-beauty-of-a-number/ 

class Solution(object):
	def divisorSubstrings(self, num, k):
		n = num
		res = 0
		div = 0
		i = 0
		while n > 0:
			div += (n % 10) * (10 ** i)
			i += 1

			if i > k:
				i -= 1
				div //= 10

			if i == k and div > 0 and num % div == 0:
				res += 1

			n //= 10

		return res
