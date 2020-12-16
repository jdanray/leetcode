# https://leetcode.com/contest/biweekly-contest-41/problems/count-the-number-of-consistent-strings/

class Solution(object):
	def countConsistentStrings(self, allowed, words):
		return sum([set(w) & set(allowed) == set(w) for w in words])
