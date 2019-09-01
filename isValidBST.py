# https://leetcode.com/problems/validate-binary-search-tree/ 

class Solution(object):
	def isValidBST(self, root):
		def inorder(root):
			if not root:
				return []
			return inorder(root.left) + [root.val] + inorder(root.right)

		tree = inorder(root)
		return len(tree) < 2 or all(tree[i] < tree[i + 1] for i in range(len(tree) - 1))

class Solution(object):
	def isValidBST(self, root):
		tree = []
		stack = []
		while root or stack:
			while root:
				stack.append(root)
				if root.left and root.left.val >= root.val:
					return False
				root = root.left

			root = stack.pop()
			if root and root.right and root.right.val < root.val:
				return False

			root = root.right

		return True 
