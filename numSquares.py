# https://leetcode.com/problems/perfect-squares/ 

class Solution(object):
	def numSquares(self, n):
		squares = []
		p = 1
		while p * p <= n:
			squares = [p * p] + squares
			p += 1

		dp = [float('inf') for _ in range(n + 1)] 
		dp[0] = 0
		for i in range(1, n + 1):
			dp[i] = 1 + min(dp[i - sq] for sq in squares if sq <= i)

		return dp[n]
