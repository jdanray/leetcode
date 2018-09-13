# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class Solution:
	def preorderTraversal(self, root):
		if not root:
			return []
		stack = [root]
		preorder = []
		while stack:
			node = stack.pop()
			if not node:
				continue
			preorder = preorder + [node.val]
			stack.append(node.right)
			stack.append(node.left)
		return preorder
