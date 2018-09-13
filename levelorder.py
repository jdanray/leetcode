# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class Solution:
	def levelOrder(self, root):
		if not root:
			return []
		order = []
		queue = [(0, root)]
		while queue:
			level, node = queue.pop(0)
			while level >= len(order):
				order.append([])
			order[level] += [node.val]
			if node.left:
				queue.append([level + 1, node.left])
			if node.right:
				queue.append([level + 1, node.right])
		return order
