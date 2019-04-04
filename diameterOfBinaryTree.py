# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
	def diameterOfBinaryTree(self, root):
		self.maxd = 0
		def maxDepth(root):
			if not root:
				return 0
			
			left = maxDepth(root.left)
			right = maxDepth(root.right)

			self.maxd = max(self.maxd, left + right)
			return max(left, right) + 1

		maxDepth(root)
		return self.maxd
