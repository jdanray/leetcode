# https://leetcode.com/problems/ugly-number/ 

class Solution(object):
	def isUgly(self, n):
		if n <= 0:
			return False

		factors = [2,3,5]
		memo = {}
		def dp(x):
			if x >= n:
				return x == n

			if x not in memo:
				memo[x] = any(dp(x * f) for f in factors)
			return memo[x] 

		return dp(1)

"""
After I solve a problem, I like to study other people's solutions. There is a simpler, more efficient solution to this problem:
"""

class Solution(object):
	def isUgly(self, num):
		if num <= 0:
			return False

		factors = [2,3,5]
		for f in factors:
			while num % f == 0:
				n //= f

		return num == 1
