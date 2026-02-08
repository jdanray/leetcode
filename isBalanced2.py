# https://leetcode.com/problems/balanced-binary-tree/

class Solution(object):
	def isBalanced(self, root):
		height = {}
		def findHeight(root):
			if not root:
				return 1
			if root not in height:
				height[root] = 1 + max(findHeight(root.left), findHeight(root.right))
			return height[root]

		def balanced(root):
			if not root:
				return True

			left = findHeight(root.left)
			right = findHeight(root.right)

			return abs(left - right) <= 1 and balanced(root.left) and balanced(root.right)

		return balanced(root)