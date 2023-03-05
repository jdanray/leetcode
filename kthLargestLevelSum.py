# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

class Solution(object):
	def kthLargestLevelSum(self, root, k):
		sums = []
		queue = collections.deque([root])
		while queue:
			s = 0
			for _ in range(len(queue)):
				node = queue.popleft()

				s += node.val

				if node.left: 
					queue.append(node.left)
				if node.right: 
					queue.append(node.right)

			sums.append(s)

		if len(sums) < k:
			return -1
		else:
			return sorted(sums)[len(sums) - k]
