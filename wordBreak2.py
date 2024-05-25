# https://leetcode.com/problems/word-break-ii/

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
