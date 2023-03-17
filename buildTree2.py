# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution(object):
	def buildTree(self, inorder, postorder):
		if not inorder or not postorder:
			return None

		rootVal = postorder[-1]
		r = 0
		while inorder[r] != rootVal:
		    r += 1

		root = TreeNode(rootVal)
		root.left = self.buildTree(inorder[:r], postorder[:r])
		root.right = self.buildTree(inorder[r + 1:], postorder[r:-1])

		return root
