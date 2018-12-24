# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		queue = [(root, [root])]
		a1 = []
		a2 = []
		while not a1 or not a2:
			node, ancestors = queue.pop(0)
			if not node:
				continue
			elif node == p:
				a1 = ancestors
			elif node == q:
				a2 = ancestors

			queue.append((node.left, ancestors + [node.left]))
			queue.append((node.right, ancestors + [node.right]))

		m = min(len(a1), len(a2)) - 1
		while a1[m] != a2[m]:
			m -= 1
		return a1[m]
