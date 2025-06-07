# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution(object):
	def smallestString(self, s):
		abc = string.ascii_lowercase
		idx = {c: i for i, c in enumerate(abc)}
		N = len(s)

		def dec(sub):
			return ''.join(abc[(idx[c] - 1) % len(abc)] for c in sub)

		i = 0
		while i < N and s[i] == 'a':
			i += 1

		if i == N:
			return s[:-1] + 'z'

		j = i
		while j < N and s[j] != 'a':
			j += 1

		return s[:i] + dec(s[i:j]) + s[j:]