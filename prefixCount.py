# https://leetcode.com/problems/counting-words-with-a-given-prefix/ 

class Solution(object):
	def prefixCount(self, words, pref):
		return sum(1 if w[:len(pref)] == pref else 0 for w in words)
