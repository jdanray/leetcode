# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

class Solution(object):
	def maxValue(self, events, k):
		N = len(events)
		events = sorted(events)

		memo = {}
		def dp(i, k):
			if i >= N or k == 0:
				return 0

			if (i, k) in memo:
				return memo[i, k]

			j = i + 1
			while j < N:
				if events[j][0] > events[i][1]:
					break
				j += 1

			memo[i, k] = max(dp(i + 1, k), events[i][2] + dp(j, k - 1))
			return memo[i, k]

		return dp(0, k)
