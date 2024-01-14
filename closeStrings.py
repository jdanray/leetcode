# https://leetcode.com/problems/determine-if-two-strings-are-close/ 

class Solution(object):
	def closeStrings(self, word1, word2):
		return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

class Solution(object):
	def closeStrings(self, word1, word2):
		return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())
