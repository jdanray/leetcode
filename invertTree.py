# https://leetcode.com/problems/invert-binary-tree/description/

class Solution(object):
	def invertTree(self, root):
		if not root:
			return None
		
		root.left, root.right = root.right, root.left
		self.invertTree(root.left)
		self.invertTree(root.right)
		return root

class Solution(object):
	def invertTree(self, root):
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.append(node.left)
				stack.append(node.right)
		return root
