# https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class Solution(object):
	def countDominantNodes(self, root):
		maxNode = dict()
		def findMax(root):
			if not root:
				return float('-inf')

			if root in maxNode:
				return maxNode[root]

			maxNode[root] = max(root.val, findMax(root.left), findMax(root.right))
			return maxNode[root]

		def count(root):
			if not root:
				return 0
			else:
				return (maxNode[root] == root.val) + count(root.left) + count(root.right)

		findMax(root)
		return count(root)