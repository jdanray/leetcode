# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class Solution(object):
	def children(self, root):
		if not root:
			return []

		return [root] + self.children(root.left) + self.children(root.right)

	def bstToGst(self, root):
		if not root:
			return None

		root.val += sum(c.val for c in self.children(root.right))
		self.bstToGst(root.right)
		self.bstToGst(root.left)
		for left in self.children(root.left):
			left.val += root.val

		return root

class Solution(object):
	def bstToGst(self, root):
		def listify(node):
			if node:
				return listify(node.left) + [node] + listify(node.right)
			else:
				return []

		nums = listify(root)
		s = 0
		for i in range(len(nums) - 1, -1, -1):
			nums[i].val += s
			s = nums[i].val

		return root
