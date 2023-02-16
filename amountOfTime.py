# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/ 

class Solution(object):
	def amountOfTime(self, root, start):
		graph = collections.defaultdict(set)
		stack = [root]
		while stack:
			node = stack.pop()

			if node.left:
				graph[node.val].add(node.left.val)
				graph[node.left.val].add(node.val)
				stack.append(node.left)

			if node.right:
				graph[node.val].add(node.right.val)
				graph[node.right.val].add(node.val)
				stack.append(node.right)

		seen = {start}
		queue = [start]
		res = -1
		while queue:
			for _ in range(len(queue)):
				u = queue.pop(0)
				for v in graph[u]:
					if v not in seen:
						queue.append(v)
						seen.add(v)                        
			res += 1

		return res
