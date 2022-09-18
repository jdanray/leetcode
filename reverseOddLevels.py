# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/ 

class Solution(object):
	def reverseOddLevels(self, root):
		level = collections.defaultdict(list)
		queue = collections.deque([[root, 0]])
		while queue:
			node, lvl = queue.popleft()

			for child in [node.left, node.right]:
				if child:
					queue.append([child, lvl + 1])
					if lvl % 2 == 0:
						level[lvl + 1].append(child)

		for l in level:
			i = 0
			j = len(level[l]) - 1
			while i < j:
				level[l][i].val, level[l][j].val = level[l][j].val, level[l][i].val
				i += 1
				j -= 1

		return root

"""
After I solve a problem, I like to study other people's solutions. I found a solution here that I wanted to preserve:

https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/discuss/2590130/Python3-BFS-with-line-by-line-comments.

The following is my (very slight) reworking of that solution:
""" 

class Solution(object):
	def reverseOddLevels(self, root):
		queue = collections.deque([root])
		level = 0 
		while queue:
			if level % 2 == 1:
				i = 0
				j = len(queue) - 1
				while i < j:
					queue[i].val, queue[j].val = queue[j].val, queue[i].val
					i += 1
					j -= 1

			for _ in range(len(queue)):
				node = queue.popleft()
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			level += 1

		return root
