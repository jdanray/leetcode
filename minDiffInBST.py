# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class Solution(object):
	def minDiffInBST(self, root):
		allnodes = []
		stack = [root]
		while stack:
			node = stack.pop()

			if not node:
				continue
		
			allnodes.append(node.val)

			stack.append(node.left)
			stack.append(node.right)

		allnodes = sorted(allnodes)
		m = None
		for i in range(1, len(allnodes)):
			d = allnodes[i] - allnodes[i - 1]
			if m == None:
				m = d
			else:
				m = min(m, d)

		return m
