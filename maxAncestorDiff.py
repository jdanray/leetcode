# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/ 

class Solution(object):
	def maxAncestorDiff(self, root):
		def helper(root):
			if not root:
				return []

			left = helper(root.left)
			right = helper(root.right)

			for node in left + right:
				d = abs(root.val - node)
				self.res = max(self.res, d)

			return [root.val] + left + right

		self.res = float('-inf')
		helper(root)
		return self.res
