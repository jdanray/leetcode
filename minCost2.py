# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/ 

class Solution(object):
	def minCost(self, s, cost):
		N = len(s)
		res = 0
		i = 1
		while i < N:
			c = cost[i - 1]
			m = cost[i - 1]
			while i < N and s[i] == s[i - 1]:
				m = max(m, cost[i])
				c += cost[i]
				i += 1

			if c != s[i - 1]:
				c -= m
				res += c

			i += 1

		return res
