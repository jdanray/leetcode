# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

class Solution(object):
	def isCompleteTree(self, root):
		if not root:
			return True

		curlevel = 0
		full = 1
		count = 0
		queue = [[root, 0, 0]]
		while queue:
			node, label, lvl = queue.pop(0)

			if lvl > curlevel:
				if count != full:
					return False
				else:
					curlevel = lvl	
					full *= 2	
					count = 0

			if label != count:
				return False
			else:
				count += 1

			if node.right and not node.left:
				return False

			if node.left:
				queue.append([node.left, label * 2, lvl + 1])
			if node.right:
				queue.append([node.right, 1 + label * 2, lvl + 1])

		return True
