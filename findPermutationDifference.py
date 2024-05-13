# https://leetcode.com/problems/permutation-difference-between-two-strings/ 

class Solution(object):
	def findPermutationDifference(self, s, t):
		sloc = {c: i for i, c in enumerate(s)}
		tloc = {c: i for i, c in enumerate(t)}
		return sum(abs(sloc[c] - tloc[c]) for c in sloc)
