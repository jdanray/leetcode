# https://leetcode.com/problems/delete-node-in-a-bst/

class Solution(object):
	def deleteNode(self, root, key):
		if not root:
			return None

		if key < root.val:
			root.left = self.deleteNode(root.left, key)
			return root

		if key > root.val:
			root.right = self.deleteNode(root.right, key)
			return root

		if not root.right:
			return root.left

		head = root.right
		while head.left:
			head = head.left

		head.left = root.left
		return root.right
