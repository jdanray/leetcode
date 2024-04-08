# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/ 

class Solution(object):
	def getSmallestString(self, s, k):
		M = len(string.ascii_lowercase)
		char2idx = {c: i for i, c in enumerate(string.ascii_lowercase)}

		res = ''
		for c in s:
			i = char2idx[c]

			if k < i and k < M - i:
				newI = i - k
				k = max(0, k - i)
			else:
				newI = 0
				k -= min(i, M - i)

			res += string.ascii_lowercase[newI]

		return res
