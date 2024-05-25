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

class Solution(object):
	def wordBreak(self, s, wordDict):
		N = len(s)
		wordDict = set(wordDict)

		dp = [False for _ in range(N + 1)]
		dp[0] = True
		for i in range(1, N + 1):
			w = ''
			for j in range(i, N + 1):
				w += s[j - 1]
				if w in wordDict and dp[i - 1]:
					dp[j] = True

		return dp[-1]
