# https://leetcode.com/problems/maximum-width-of-binary-tree/

class Solution:
	def widthOfBinaryTree(self, root):
		if not root:
			return 0

		widths = dict()
		stack = [(1, 1, root)]
		while stack:
			level, pos, node = stack.pop()
			if not node:
				continue

			if level in widths:
				widths[level].append(pos)
			else:
				widths[level] = [pos]

			k = 2 * pos
			stack.append((level + 1, k - 1, node.left))
			stack.append((level + 1, k, node.right))
		
		return max(max(widths[w]) - min(widths[w]) for w in widths) + 1

"""
This is an improvement on the previous solution
The code is prettier and simpler, and the program uses less space

Invariants:
-Of course, curlevel represents the current level
-For each curlevel, leftpos/rightpos represents the position of the leftmost/rightmost node on that level
	Initially, they both equal 1. At the first level, there's only root, and it's both the leftmost and rightmost node
	As we scan a level, rightpos must change 
-maxwidth represents the maximum width we've seen so far while scanning levels
-width is equal to the difference between the leftmost node and the rightmost node
	It increases as we scan a level
	We always scan the whole level, so we find the biggest width for each level

We use BFS, so the first time we encounter a node on a next level, we know we've moved on to that level
	So, update curlevel and leftpos
The BFS runs left to right, which makes it easier to keep track of leftpos and rightpos
"""

class Solution:
	def widthOfBinaryTree(self, root):
		maxwidth = 0
		leftpos = 1
		rightpos = 1
		curlevel = 1
		queue = [(curlevel, leftpos, root)]
		while queue:
			lvl, pos, node = queue.pop(0)
			if not node:
				continue

			rightpos = pos
			if lvl == curlevel + 1:
				leftpos = pos
				curlevel = lvl

			width = rightpos - leftpos + 1
			maxwidth = max(maxwidth, width)

			childpos = 2 * pos
			queue.append((lvl + 1, childpos - 1, node.left))
			queue.append((lvl + 1, childpos, node.right))
		
		return maxwidth

# New solution
# Don't need to keep track of the current level

class Solution(object):
	def widthOfBinaryTree(self, root):
		queue = collections.deque([[root, 1]])
		res = 0
		while queue:
			left = -1
			right = -1
			for _ in range(len(queue)):
				node, pos = queue.popleft()

				if not node:
					continue

				if left == -1:
					left = pos
				right = pos

				queue.append([node.left, pos * 2])
				queue.append([node.right, pos * 2 + 1])

			res = max(res, right - left + 1)

		return res
