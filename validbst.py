# https://leetcode.com/problems/validate-binary-search-tree/description/

class Solution:
	def isValidBST(self, root):
		if not root:
			return True
		elif self.helper(root.left, root.val, 'lt') and self.helper(root.right, root.val, 'gt'):
			return self.isValidBST(root.left) and self.isValidBST(root.right)
		else:
			return False

	def helper(self, node, val, op):
		if not node:
			return True
		elif op == 'gt':
			return node.val > val and self.helper(node.left, val, op) and self.helper(node.right, val, op)
		else:
			return node.val < val and self.helper(node.left, val, op) and self.helper(node.right, val, op)

	
		
