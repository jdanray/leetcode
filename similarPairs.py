# https://leetcode.com/problems/count-pairs-of-similar-strings/ 

class Solution(object):
	def similarPairs(self, words):
		place = {c: i for i, c in enumerate(string.ascii_lowercase)}

		count = collections.Counter()
		res = 0
		for w in words:
			chars = 0
			for c in w:
				chars |= (1 << place[c])

			if chars in count:
				res += count[chars]

			count[chars] += 1

		return res
