# https://leetcode.com/problems/substring-with-concatenation-of-all-words/ 

class Solution(object):
	def findSubstring(self, s, words):
		if not s or not words:
			return []

		res = []
		N = len(words)
		l = len(words[0])
		count = collections.Counter(words)
		for i in range(len(s) - l * N + 1):
			seen = collections.Counter()
			for j in range(N):
				k = i + (j * l)
				w = s[k:k + l]
				seen[w] += 1

			if seen == count:
				res.append(i)

		return res
