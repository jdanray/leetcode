# https://leetcode.com/problems/count-prefixes-of-a-given-string/ 

class Solution(object):
	def countPrefixes(self, words, s):
		return len([w for w in words if s[:len(w)] == w])
