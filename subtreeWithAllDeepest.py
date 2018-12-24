# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

class Solution(object):
	def subtreeWithAllDeepest(self, root):
		if not root:
			return None

		parent = {root: None}
		deepest = {root}
		curlevel = 0
		queue = [[root, curlevel]]

		while queue:
			node, level = queue.pop(0)

			if level > curlevel:
				curlevel = level
				deepest = {node}
			else:
				deepest.add(node)

			if node.left:
				parent[node.left] = node
				queue.append([node.left, level + 1])

			if node.right:
				parent[node.right] = node
				queue.append([node.right, level + 1])

		while len(deepest) != 1:
			deepest = {parent[d] for d in deepest}

		return deepest.pop()

class Solution:
	def subtreeWithAllDeepest(self, root):
		queue = [(root, [root])]
		deepest = []
		maxdepth = 0
		while queue:
			node, ancestors = queue.pop(0)
			if not node:
				continue

			if len(ancestors) > maxdepth:
				maxdepth = len(ancestors)
				deepest = [ancestors]
			elif len(ancestors) == maxdepth:
				deepest.append(ancestors)

			queue.append((node.left, ancestors + [node.left]))
			queue.append((node.right, ancestors + [node.right]))

		m = min(len(d) for d in deepest) - 1
		while any(a1[m] != a2[m] for a1 in deepest for a2 in deepest):
			m -= 1
		return deepest[0][m]
