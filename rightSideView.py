# https://leetcode.com/problems/binary-tree-right-side-view/description/ 

class Solution(object):
	def rightSideView(self, root):
		if not root:
			return []

		view = []
		rightmost = root.val
		curlevel = 0
		queue = [(curlevel, root)]

		while queue:
			level, node = queue.pop(0)

			if not node:
				continue

			if level > curlevel:
				curlevel = level
				view.append(rightmost)

			rightmost = node.val

			queue.append((level + 1, node.left))
			queue.append((level + 1, node.right))

		view.append(rightmost)
		return view
