# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/ 

class Solution(object):
	def isAcronym(self, words, s):
		return len(words) == len(s) and all(s[i] == w[0] for i, w in enumerate(words))
