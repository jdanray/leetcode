# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Solution(object):
	def buildTree(self, preorder, inorder):
		if not preorder:
			return None

		headval = preorder[0]
		inleft = []
		seen = set()
		i = 0
		while i < len(inorder) and inorder[i] != headval:
			seen.add(inorder[i])
			inleft.append(inorder[i])
			i += 1
		inright = inorder[i + 1:]

		j = 1
		preleft = []
		while j < len(preorder) and preorder[j] in seen:
			preleft.append(preorder[j])
			j += 1
		preright = preorder[j:]

		head = TreeNode(headval)
		head.left = self.buildTree(preleft, inleft)
		head.right = self.buildTree(preright, inright)

		return head
