# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution(object):
	def areOccurrencesEqual(self, s):
		return len(set(collections.Counter(s).values())) == 1
