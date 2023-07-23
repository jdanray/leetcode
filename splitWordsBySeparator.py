# https://leetcode.com/problems/split-strings-by-separator/ 

class Solution(object):
	def splitWordsBySeparator(self, words, separator):
		res = []
		for w in words:
			for s in w.split(separator):
				if s:
					res.append(s)
		return res
