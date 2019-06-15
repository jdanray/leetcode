# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution(object):
	def distanceK(self, root, target, K):
		graph = collections.defaultdict(set)
		def build(node):
			if node:
				graph[node].add(node.left)
				graph[node].add(node.right)
				graph[node.left].add(node)
				graph[node.right].add(node)
				build(node.left)
				build(node.right)

		build(root)
		queue = [[target, 0]]
		seen = {target}
		res = []
		while queue:
			node, dist = queue.pop(0)

			if not node:
				continue

			if dist == K:
				res = [node.val] + res
				continue

			for u in graph[node]:
				if u not in seen:
					seen.add(u)
					queue.append([u, dist + 1])

		return res
