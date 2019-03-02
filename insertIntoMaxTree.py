# https://leetcode.com/problems/maximum-binary-tree-ii/

class Solution(object):
	def insertIntoMaxTree(self, root, val):
		if not root or val > root.val:
			newroot = TreeNode(val)
			newroot.left = root
			return newroot
		
		root.right = self.insertIntoMaxTree(root.right, val)
		return root

