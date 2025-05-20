# https://leetcode.com/problems/find-mirror-score-of-a-string/

class Solution(object):
	def calculateScore(self, s):
		char2idx = {c: i for i, c in enumerate(string.ascii_lowercase)}
		mirror = collections.defaultdict(list)
		res = 0
		for i, c in enumerate(s):
			r = string.ascii_lowercase[-char2idx[c] - 1]
			if mirror[r]:
				j = mirror[r].pop()
				res += i - j
			else:
				mirror[c].append(i)

		return res
