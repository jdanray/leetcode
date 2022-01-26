# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/ 

class Solution(object):
	def minimumCost(self, cost):
		N = len(cost)
		res = 0
		cost = sorted(cost, reverse=True)
		for i in range(0, N, 3):
			res += cost[i]
			if i + 1 < N:
				res += cost[i + 1]
                
		return res

"""
After I solve a problem, I like to study other people's solutions.

I found a more concise implementation of the same idea here: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/discuss/1709892/JavaC%2B%2BPython-Easy-and-Consice
"""

class Solution(object):
	def minimumCost(self, A):
		return sum(a for i,a in enumerate(sorted(A)) if (len(A) - i) % 3)
