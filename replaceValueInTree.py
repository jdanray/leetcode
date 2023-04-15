# https://leetcode.com/problems/cousins-in-binary-tree-ii/ 

class Solution(object):
	def replaceValueInTree(self, root):
		queue = collections.deque([[root, 0]])
		while queue:
			s = 0
			for _ in range(len(queue)):
				node, sib = queue.popleft()

				if not node:
					continue

				s += node.val

				queue.append((node, sib))

			for _ in range(len(queue)):
				node, sib = queue.popleft()

				node.val = s - node.val - sib

				queue.append((node.left, node.right.val if node.right else 0))
				queue.append((node.right, node.left.val if node.left else 0))

		return root
