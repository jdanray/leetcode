# https://leetcode.com/problems/print-binary-tree/

class Solution(object):
	def height(self, root):
		if not root:
			return 0

		return 1 + max(self.height(root.left), self.height(root.right))

	def printTree(self, root):
		nrows = self.height(root)
		ncols = 2 ** nrows - 1 

		tree = [["" for _ in range(ncols)] for _ in range(nrows)]
		stack = [[root, 0, 0, ncols - 1]]
		while stack:
			node, row, left, right = stack.pop()

			if not node:
				continue

			col = left + (right - left) // 2
			tree[row][col] = str(node.val)

			stack.append([node.left, row + 1, left, col - 1])
			stack.append([node.right, row + 1, col + 1, right])
 
		return tree
