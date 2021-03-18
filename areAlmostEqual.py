# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/ 

class Solution(object):
	def areAlmostEqual(self, s1, s2):
		return collections.Counter(s1) == collections.Counter(s2) and sum(s1[i] != s2[i] for i in range(len(s1))) in [0, 2]
