# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

"""
The basic idea is inductive:

path(node) =	{ [node], if the node is the root
		{ path(parent(node)) + [node], otherwise

The (not-so-great) difficulty lies in finding a given node's parent. To find a given node's parent, you can exploit the fact that you are considering a full binary tree:
"""

class Solution(object):
	def pathInZigZagTree(self, label):
		row = 0
		l = label
		while l > 0:
			l >>= 1
			row += 1

		lower = 2 ** (row - 1)
		upper = 2 ** row - 1

		if row % 2 == 0:
			dist = label - lower
		else:
			dist = upper - label

		path = []
		while label >= 1:
			path = [label] + path

			dist >>= 1
			upper = lower - 1
			lower >>= 1
			row -= 1

			if row % 2 == 0:
				label = lower + dist
			else:
				label = upper - dist

		return path
