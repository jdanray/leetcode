# https://leetcode.com/problems/expressive-words/

class Solution:
	def group(self, s):
		g = [1 for _ in range(len(s))]
		for i in range(len(s) - 2, -1, -1):
			if s[i] == s[i + 1]:
				g[i] = g[i + 1] + 1
		return g

	def stretchy(self, S, slen, w):
		wlen = self.group(w)
		i = 0
		j = 0
		while i < len(S) and j < len(w):
			if S[i] != w[j] or slen[i] < wlen[j] or (slen[i] != wlen[j] and slen[i] < 3):
				return False

			i += slen[i]
			j += wlen[j]

		return i == len(S) and j == len(w)

	def expressiveWords(self, S, words):
		return sum(1 if self.stretchy(S, self.group(S), w) else 0 for w in words)

class Solution:
	def group(self, s):
		g = [1 for _ in range(len(s))]
		for i in range(len(s) - 2, -1, -1):
			if s[i] == s[i + 1]:
				g[i] = g[i + 1] + 1
		return g

	def expressiveWords(self, S, words):
		slen = self.group(S)
		nstretch = 0
		for w in words:
			wlen = self.group(w)
			i = 0
			j = 0
			while i < len(S) and j < len(w):
				if S[i] != w[j] or slen[i] < wlen[j]:
					break
				elif slen[i] == wlen[j] or slen[i] >= 3:
					i += slen[i]
					j += wlen[j]
				else: 
					break

			if i == len(S) and j == len(w):
				nstretch += 1

		return nstretch
