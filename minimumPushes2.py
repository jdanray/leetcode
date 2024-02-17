# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/ 

class Solution(object):
	def minimumPushes(self, word):
		K = 8

		count = collections.Counter(word)
		chars = sorted(count.keys(), key=lambda x: count[x], reverse=True)
		res = 0
		for i, c in enumerate(chars):
			res += (i // K + 1) * count[c]

		return res
