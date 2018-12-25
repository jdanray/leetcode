# https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution(object):
	def findLUSlength(self, A, B):
		return -1 if A == B else max(len(A), len(B))
