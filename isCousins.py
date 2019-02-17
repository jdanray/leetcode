# https://leetcode.com/problems/cousins-in-binary-tree/ 

class Solution(object):
	def isCousins(self, root, x, y):
		cuz = [-1, -1]
		queue = [[root, 0, 0]]
		while queue:
			node, depth, parent = queue.pop(0)
		
			if not node:
				continue

			if node.val == x or node.val == y:
				if cuz == [-1, -1]:
					cuz = [depth, parent]
				else:
					return cuz[0] == depth and cuz[1] != parent

			queue.append([node.left, depth + 1, node.val])
			queue.append([node.right, depth + 1, node.val])

