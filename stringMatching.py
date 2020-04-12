# https://leetcode.com/problems/string-matching-in-an-array/ 

class Solution(object):
	def stringMatching(self, words):
		res = set()
		for i, wi in enumerate(words):
			for j, wj in enumerate(words):
				if i != j and len(wj) > len(wi) and wi in wj:
					res.add(wi)
		return list(res)
