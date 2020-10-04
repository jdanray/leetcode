# https://leetcode.com/problems/even-odd-tree/ 

class Solution(object):
	def isEvenOddTree(self, root):
		prevnode = None
		level = -1
		queue = [[root, 0]]
		while queue:
			node, curlvl = queue.pop(0)

			if not node:
				continue

			if curlvl % 2 == node.val % 2:
				return False

			if level == curlvl:
				if level % 2 == 0 and node.val <= prevnode.val:
					return False
				elif level % 2 == 1 and node.val >= prevnode.val:
					return False

			level = curlvl
			prevnode = node

			queue.append([node.left, curlvl + 1])
			queue.append([node.right, curlvl + 1])

		return True
