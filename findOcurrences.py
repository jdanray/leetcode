# https://leetcode.com/problems/occurrences-after-bigram/

class Solution(object):
	def findOcurrences(self, text, first, second):
		text = text.split()
		return [text[i + 2] for i in range(len(text) - 2) if text[i] == first and text[i + 1] == second]
