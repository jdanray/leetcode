# https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution(object):
	def minCuttingCost(self, n, m, k):
		return sum((x - k) * (x - (x - k)) for x in [m, n] if x > k)