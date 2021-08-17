# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/ 

class Solution(object):
	def numOfStrings(self, patterns, word):
		return len([p for p in patterns if p in word])
