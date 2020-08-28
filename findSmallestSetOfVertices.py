# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution(object):
	def findSmallestSetOfVertices(self, n, edges):
		allnodes = set(range(n))
		tonodes = {v for _, v in edges}
		return list(allnodes - tonodes)
