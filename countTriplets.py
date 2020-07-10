# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/ 

class Solution(object):
	def countTriplets(self, A):
		doubles = collections.Counter(a & b for a in A for b in A)
		res = 0
		for a in A:
			for d in doubles:
				if a & d == 0:
					res += doubles[d]
		return res
