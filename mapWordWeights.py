# https://leetcode.com/problems/weighted-word-mapping/

class Solution(object):
	def mapWordWeights(self, words, weights):
		abc = string.ascii_lowercase
		weight = {c: weights[i] for i, c in enumerate(abc)}

		res = ''
		for w in words:
			wt = sum(weight[c] for c in w) % len(weight)
			res += abc[-wt - 1]

		return res

class Solution(object):
	def mapWordWeights(self, words, weights):
		abc = string.ascii_lowercase
		weight = {c: weights[i] for i, c in enumerate(abc)}
		return ''.join(abc[-sum(weight[c] for c in w) % len(weight) - 1] for w in words)