# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

class Solution(object):
	def levelOrderBottom(self, root):
		if not root:
			return []

		order = [[]]
		queue = [[root, 0]]
		curlevel = 0
		while queue:
			node, level = queue.pop(0)

			if not node:
				continue

			if level > curlevel:
				curlevel = level
				order = [[]] + order

			order[0].append(node.val)

			queue.append([node.left, level + 1])
			queue.append([node.right, level + 1])

		return order
