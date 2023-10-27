# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution(object):
	def mincostTickets(self, days, costs):
		def consec(d, n):
			k = d + 1
			while k < len(days) and days[k] - days[d] < n:
				k += 1
			return k

		memo = {}
		def mincost(d):
			if d >= len(days):
				return 0

			if d not in memo:
				a = costs[0] + mincost(d + 1)
				b = costs[1] + mincost(consec(d, 7))
				c = costs[2] + mincost(consec(d, 30))
				memo[d] = min(a, b, c)
			return memo[d]

		return mincost(0)

# After I solve a problem, I like to study other people's solutions to the same problem.
# The following is the top-voted solution, translated by me from Java into Python.
# Link to original: https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226670/Java-DP-Solution-with-explanation-O(n)

class Solution(object):
	def mincostTickets(self, days, costs):
		days = set(days)
		N = 365
		mincost = [0 for _ in range(N + 1)]
		for d in range(1, N + 1):
			if d not in days:
				mincost[d] = mincost[d - 1]
			else:
				a = costs[0] + mincost[d - 1]
				b = costs[1] + mincost[max(d - 7, 0)]
				c = costs[2] + mincost[max(d - 30, 0)]
				mincost[d] = min(a, b, c)
		return mincost[365]

# Another top-down solution 
class Solution(object):
	def mincostTickets(self, days, costs):
		passes = [1, 7, 30]

		memo = {}
		def dp(i):
			if i >= len(days):
				return 0

			if i in memo:
				return memo[i]

			res = float('inf')
			for j, p in enumerate(passes):
				k = i + 1
				while k < len(days) and days[k] < days[i] + p:
					k += 1

				res = min(res, costs[j] + dp(k))

			memo[i] = res
			return memo[i]

		return dp(0)
