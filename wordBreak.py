# https://leetcode.com/problems/word-break/ 

class Solution(object):
	def wordBreak(self, s, wordDict):
		N = len(s)
		wordDict = set(wordDict)

		memo = {}
		def dp(i):
			if i >= N:
				return True

			if i in memo:
				return memo[i]

			w = ''
			for j in range(i, N):
				w += s[j]
				if w in wordDict and dp(j + 1):
					memo[i] = True
					return memo[i]

			memo[i] = False
			return memo[i]

		return dp(0)
