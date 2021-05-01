# https://leetcode.com/problems/sum-of-digits-in-base-k/ 

class Solution(object):
	def sumBase(self, n, k):
		res = 0
		while n > 0:
			res += n % k
			n //= k
		return res
