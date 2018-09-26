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

class Solution:
	def sumOfLeftLeaves(self, root):
		if not root:
			return 0

		s = 0
		if root.left and not (root.left.left or root.left.right):
			s += root.left.val
		if root.left:
			s += self.sumOfLeftLeaves(root.left)
		if root.right:
			s += self.sumOfLeftLeaves(root.right)

		return s
