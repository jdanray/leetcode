# https://leetcode.com/problems/delete-nodes-and-return-forest/

class Solution(object):
	def delNodes(self, root, to_delete):
		to_delete = set(to_delete)

		res = []
		def prune(node, isstart):
			if not node:
				return False

			if node.val in to_delete:
				prune(node.left, True)
				prune(node.right, True)
				return False

			if isstart:
				res.append(node)

			if node.left and node.left.val in to_delete:
				prune(node.left, True)
				node.left = None
			else:
				prune(node.left, False)

			if node.right and node.right.val in to_delete:
				prune(node.right, True)
				node.right = None
			else:
				prune(node.right, False)

		prune(root, True)
		return res

"""
After I solve a problem, I like to examine other people's solutions to the problem.

The following solution is based on exactly the same idea that my solution is based on, but the implementation is neater: 

Source: https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution
"""

class Solution(object):
	def delNodes(self, root, to_delete):
		to_delete_set = set(to_delete)
		res = []
		
		def helper(root, is_root):
			if not root: return None
			root_deleted = root.val in to_delete_set
			if is_root and not root_deleted:
				res.append(root)
			root.left = helper(root.left, root_deleted)
			root.right = helper(root.right, root_deleted)
			return None if root_deleted else root
		helper(root, True)
		return res
