# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution(object):
	def countCharacters(self, words, chars):
		res = 0
		chcount = collections.Counter(chars)
		for wd in words:
			wdcount = collections.Counter(wd)
			if all(chcount[c] >= wdcount[c] for c in wdcount):
				res += len(wd)
		return res
