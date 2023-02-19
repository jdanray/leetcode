# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/ 

class Solution(object):
	def zigzagLevelOrder(self, root):
		if not root:
			return []

		result = []
		rank = []
		zig = True
		curlevel = 0
		queue = [[root, curlevel]]

		while queue:
			node, level = queue.pop(0)

			if not node:
				continue

			if level > curlevel:
				curlevel = level
				result.append(rank)
				rank = []
				zig = not zig

			if zig:
				rank += [node.val]
			else:
				rank = [node.val] + rank

			queue.append([node.left, level + 1])
			queue.append([node.right, level + 1])

		result.append(rank)
		return result

class Solution(object):
	def zigzagLevelOrder(self, root):
		if not root:
			return []

		res = []
		zig = True
		queue = collections.deque([root])
		while queue:
			rank = []
			for _ in range(len(queue)):
				node = queue.popleft()

				if zig:
					rank += [node.val]
				else:
					rank = [node.val] + rank

				if node.left: 
					queue.append(node.left)
				if node.right: 
					queue.append(node.right)

			res.append(rank)
			zig = not zig

		return res
