# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

class Solution:
	def flatten(self, root):
		prev = None
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				stack.append(node.right)
				stack.append(node.left)
				node.left = None
				if prev: 
					prev.right = node
				prev = node
