# https://leetcode.com/problems/binary-tree-pruning/description/

class Solution:
	def pruneTree(self, root):
		if not root:
			return None
		left = pruneTree(root.left)
		right = pruneTree(root.right)
		if left == None and right == None and root.val == 0:
			return None
		if left == None:
			root.left = None
		if right == None:
			root.right = None
		return root
