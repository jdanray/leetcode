# https://leetcode.com/problems/extra-characters-in-a-string/ 

class Solution(object):
	def minExtraChar(self, s, dictionary):
		N = len(s)
		dictionary = set(dictionary)

		memo = {}
		def dp(start):
			if start >= N:
				return 0

			if start in memo:
				return memo[start]

			sub = ''
			extra = 0
			res = float('inf')
			for i in range(start, N):
				sub += s[i]
				extra += 1

				if sub in dictionary:
					res = min(res, dp(i + 1))

				res = min(res, extra + dp(i + 1))

			memo[start] = res
			return memo[start]

		return dp(0)
