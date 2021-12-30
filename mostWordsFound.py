# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/ 

class Solution(object):
	def mostWordsFound(self, sentences):
		return max(len(s.split()) for s in sentences)
