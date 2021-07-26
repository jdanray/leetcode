# https://leetcode.com/problems/maximum-compatibility-score-sum/

class Solution(object):
	def maxCompatibilitySum(self, students, mentors):
		M = len(students)
		N = len(students[0])

		comp = [[0 for _ in range(M)] for _ in range(M)]
		for i, s in enumerate(students):
			for j, m in enumerate(mentors):
				comp[i][j] = sum(1 if s[k] == m[k] else 0 for k in range(N))

		memo = {}
		def dp(i, used):
			if i >= M:
				return 0
			elif (i, used) in memo:
				return memo[i, used]

			res = 0
			for j in range(M):
				if (used >> j) & 1 == 0:
					res = max(res, comp[i][j] + dp(i + 1, used | (1 << j)))

			memo[i, used] = res
			return memo[i, used]

		return dp(0, 0)
