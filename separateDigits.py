# https://leetcode.com/problems/separate-the-digits-in-an-array/ 

class Solution(object):
	def separateDigits(self, nums):
		res = []
		for n in nums:
			digs = []
			while n > 0:
				d = n % 10
				digs = [n] + digs
				n //= 10
			res += digs

		return res
