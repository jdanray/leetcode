class Solution(object):
	def searchBST(self, root, val):
		if not root:
			return None
		elf val == root.val:
			return root
		elif val < root.val:
			return self.searchBST(root.left, val)
		else:
			return self.searchBST(root.right, val)
