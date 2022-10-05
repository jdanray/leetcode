# https://leetcode.com/problems/add-one-row-to-tree/

class Solution(object):
	def addOneRow(self, root, v, d):
		if not root:
			return None

		if d == 1:
			newroot = TreeNode(v)
			newroot.left = root
			root = newroot
		elif d == 2:
			l = TreeNode(v)
			r = TreeNode(v)
			l.left = root.left
			r.right = root.right
			root.left = l
			root.right = r

		self.addOneRow(root.left, v, d - 1)
		self.addOneRow(root.right, v, d - 1)

		return root
