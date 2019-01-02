# https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution(object):
	def searchBST(self, root, val):
		if not root:
			return None
		elif val == root.val:
			return root
		elif val < root.val:
			return self.searchBST(root.left, val)
		else:
			return self.searchBST(root.right, val)

class Solution(object):
	def searchBST(self, root, val):
		while root and val != root.val:
			root = root.left if val < root.val else root.right
		return root
