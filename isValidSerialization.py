# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/

class Solution(object):
	def isValidSerialization(self, preorder):
		preorder = preorder.split(',')
		nleaves = 0
		ninternals = 0
		i = 0
		while i < len(preorder) and nleaves <= ninternals:
			c = preorder[i]
			if c == '#':
				nleaves += 1
			else:
				ninternals += 1
			i += 1
		return i == len(preorder) and nleaves == ninternals + 1
