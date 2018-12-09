# https://leetcode.com/problems/trim-a-binary-search-tree/

class Solution:
	def trimBST(self, root, L, R):
		if not root:
			return None
		elif L <= root.val <= R:
			root.left = self.trimBST(root.left, L, R)
			root.right = self.trimBST(root.right, L, R)
			return root
		elif root.val < L:
			return self.trimBST(root.right, L, R)
		elif root.val > R:
			return self.trimBST(root.left, L, R)
