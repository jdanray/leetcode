# https://leetcode.com/problems/find-mirror-score-of-a-string/

class Solution(object):
	def calculateScore(self, s):
		char2idx = {c: i for i, c in enumerate(string.ascii_lowercase)}
		def reflect(c): 
			i = char2idx[c]
			return string.ascii_lowercase[len(string.ascii_lowercase) - i - 1]

		mirror = collections.defaultdict(list)
		res = 0
		for i, c in enumerate(s):
			r = reflect(c)
			if mirror[r]:
				j = mirror[r].pop()
				res += i - j				
			else:
				mirror[c].append(i)

		return res