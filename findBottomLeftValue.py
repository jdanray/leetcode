# https://leetcode.com/problems/find-bottom-left-tree-value/description/

class Solution(object):
	def findBottomLeftValue(self, root):
		curlevel = 0
		bottomleft = root.val
		queue = [[root, curlevel]]
		while queue:
			node, level = queue.pop(0)

			if not node:
				continue

			if level > curlevel:
				curlevel = level
				bottomleft = node.val

			queue.append([node.left, level + 1])
			queue.append([node.right, level + 1])

		return bottomleft 

"""
After I solve a problem, I like to review other people's solutions
So, the following isn't my solution, but it's too cool to not preserve for posterity
It does a right-to-left BFS. So, the last node visited must be the bottom left node.
"""

class Solution:
	def findLeftMostNode(self, root):
		queue = [root]
		for node in queue:
			queue += filter(None, (node.right, node.left))
		return node.val
