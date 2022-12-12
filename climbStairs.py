# https://leetcode.com/problems/climbing-stairs/ 

class Solution(object):
	def climbStairs(self, n):
		memo = {1: 1, 2: 2}
		for i in range(3, n + 1):
			memo[i] = memo[i - 1] + memo[i - 2]
		return memo[n]

class Solution(object):
	def climbStairs(self, n):
		a = 1
		b = 1
		for _ in range(2, n + 1):
			a, b = b, a + b
		return b
