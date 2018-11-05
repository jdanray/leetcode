# https://leetcode.com/problems/4sum-ii/description/

class Solution(object):
	def fourSumCount(self, A, B, C, D):
		S = dict()
		for a in A:
			for b in B:
				s = a + b
				if s in S:
					S[s] += 1
				else:
					S[s] = 1

		ntuples = 0
		for c in C:
			for d in D:
				t = -c - d
				if t in S:
					ntuples += S[t]

		return ntuples

"""
After I solve a problem, I like to examine other people's solutions
The following is code that was too good not to preserve
"""

from collections import Counter

class Solution(object):
	def fourSumCount(self, A, B, C, D):
		AB = Counter(a + b for a in A for b in B)
		return sum(AB[-c - d] for c in C for d in D) 
