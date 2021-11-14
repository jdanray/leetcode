# https://leetcode.com/problems/two-best-non-overlapping-events/ 

class Solution(object):
	def maxTaxiEarnings(self, n, rides):
		passengers = collections.defaultdict(list)
		for (start, end, tip) in rides:
			passengers[start].append([end, tip])

		memo = {}
		def dp(start):
			if start >= n:
				return 0

			if start in memo:
				return memo[start]

			memo[start] = dp(start + 1)
			for (end, tip) in passengers[start]:
				memo[start] = max(memo[start], dp(end) + (end - start + tip))

			return memo[start]

		return dp(1)
