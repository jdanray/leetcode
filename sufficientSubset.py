# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

class Solution(object):
	def sufficientSubset(self, root, limit):
		if root.left == None and root.right == None:
			if root.val < limit:
				return None
			else:
				return root

		if root.left:
			root.left = self.sufficientSubset(root.left, limit - root.val)

		if root.right:
			root.right = self.sufficientSubset(root.right, limit - root.val)

		if root.left or root.right:
			return root

		return None
