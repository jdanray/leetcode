# https://leetcode.com/problems/leaf-similar-trees/description/

class Solution:
	def leafSeq(self, root):
		if not root:
			return []

		seq = []
		stack = [root]
		while stack:
			node = stack.pop()
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
			if not (node.left or node.right):
				seq.append(node.val)

		return seq
				
	def leafSimilar(self, root1, root2):
		return self.leafSeq(root1) == self.leafSeq(root2)
