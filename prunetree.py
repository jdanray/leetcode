# https://leetcode.com/problems/binary-tree-pruning/description/

class Solution:
	def pruneTree(self, root):
		if not root:
			return None

		root.left = self.pruneTree(root.left)
		root.right = self.pruneTree(root.right)
		return root if (root.val == 1 or root.left or root.right) else None

class Solution:
	def pruneTree(self, root):
		if not root:
			return None

		left = self.pruneTree(root.left)
		right = self.pruneTree(root.right)
		
		if not left:
			root.left = None
		if not right:
			root.right = None
		
		if root.val == 0 and not left and not right:
			return None
		else:
			return root	

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

class Solution:
	def pruneTree(self, root):
		if not root:
			return None

		if self.noOnes(root.left):
			root.left = None
		if self.noOnes(root.right):
			root.right = None

		self.pruneTree(root.left)
		self.pruneTree(root.right)

		return root

	def noOnes(self, root):
		if not root:
			return True
		else:
			return root.val != 1 and self.noOnes(root.left) and self.noOnes(root.right)
