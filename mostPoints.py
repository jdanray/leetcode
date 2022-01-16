# https://leetcode.com/problems/solving-questions-with-brainpower/ 

class Solution(object):
	def mostPoints(self, questions):
		N = len(questions)

		memo = {}
		def dp(i):
			if i >= N:
				return 0

			if i in memo:
				return memo[i]

			solve = questions[i][0] + dp(i + 1 + questions[i][1])
			skip = dp(i + 1)

			memo[i] = max(solve, skip)
			return memo[i]

		return dp(0)
