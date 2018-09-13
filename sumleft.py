# https://leetcode.com/problems/sum-of-left-leaves/description/

class Solution:
	def sumOfLeftLeaves(self, root):
		if not root:
			return 0
		s = 0
		stack = [root]
		while stack:
			node = stack.pop()
			if node.left and not (node.left.left or node.left.right):
				s += node.left.val
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		return s
