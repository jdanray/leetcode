# https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution(object):
	def minimumOperations(self, nums, start, goal):
		LOWER = 0
		UPPER = 1000

		queue = deque([[start, 0]])
		visited = set()
        
		while queue:
			node, ops = queue.popleft()

			if node == goal:
				return ops

			if node < LOWER or node > UPPER or node in visited:
				continue

			visited.add(node)

			for n in nums:
				queue.append((node + n, ops + 1))
				queue.append((node - n, ops + 1))
				queue.append((node ^ n, ops + 1))

		return -1
