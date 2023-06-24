# https://leetcode.com/problems/decremental-string-concatenation/ 

class Solution(object):
	def minimizeConcatenatedLength(self, words):
		@functools.lru_cache(None)
		def dp(i, first, last):
			if i >= len(words):
				return 0

			pre = len(words[i]) + dp(i + 1, words[i][0], last)
			if first == words[i][-1]:
				pre -= 1

			post = len(words[i]) + dp(i + 1, first, words[i][-1])
			if last == words[i][0]:
				post -= 1

			return min(pre, post)

		return len(words[0]) + dp(1, words[0][0], words[0][-1])
