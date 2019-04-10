# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

class Solution:
	def bstFromPreorder(self, preorder):
		def bst(i, j):
			if i >= j:
				return None

			k = i + 1
			while k < len(preorder) and preorder[i] > preorder[k]:
				k += 1

			root = TreeNode(preorder[i])
			root.left = bst(i + 1, k)
			root.right = bst(k, j)

			return root

		return bst(0, len(preorder))

class Solution:
	def bstFromPreorder(self, preorder):
		if not preorder:
			return None

		i = 1
		while i < len(preorder) and preorder[0] > preorder[i]:
			i += 1

		root = TreeNode(preorder[0])
		root.left = self.bstFromPreorder(preorder[1:i])
		root.right = self.bstFromPreorder(preorder[i:])

		return root
