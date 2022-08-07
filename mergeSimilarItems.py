# https://leetcode.com/problems/merge-similar-items/ 

class Solution(object):
	def mergeSimilarItems(self, items1, items2):
		L = 1000

		d = collections.defaultdict(int)
		for (v, w) in items1 + items2:
			d[v] += w

		return [[v, d[v]] for v in range(1, L+1) if v in d]
