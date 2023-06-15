# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class Solution(object):
	def maxLevelSum(self, root):
		curlevel = 1
		cursum = 0
		maxlevel = 1
		maxsum = 0

		queue = [[root, curlevel]]
		while queue:
			node, lvl = queue.pop(0)

			if not node:
				continue

			if lvl > curlevel:
				if cursum > maxsum:
					maxsum = cursum
					maxlevel = curlevel
				curlevel = lvl
				cursum = 0

			cursum += node.val

			queue.append([node.left, lvl + 1])
			queue.append([node.right, lvl + 1])

		if cursum > maxsum:
			maxlevel = curlevel

		return maxlevel

class Solution(object):
	def maxLevelSum(self, root):
		level = 1
		res = 1
		maxSum = -float('inf')
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

			if s > maxSum:
				maxSum = s
				res = level

			level += 1

		return res
