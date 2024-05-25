# https://leetcode.com/problems/word-break/ 

class Solution(object):
	def wordBreak(self, s, wordDict):
		wordDict = set(wordDict)

		def backtrack(i):
			if i >= len(s):
				return [[]]

			w = ''
			res = []
			for j in range(i, len(s)):
				w += s[j]
				if w in wordDict:
					for words in backtrack(j + 1):
						res.append([w] + words)
			return res

		return [' '.join(words) for words in backtrack(0)]

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
