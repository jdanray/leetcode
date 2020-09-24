# https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution(object):
	def reorderSpaces(self, text):
		space = " "
		ns = text.count(space)
		
		words = text.split()
		nw = len(words) - 1

		ngaps = 0 if nw == 0 else ns // nw
		nend = ns if nw == 0 else ns % nw

		res = (space * ngaps).join(words) + (space * nend)
		return res
