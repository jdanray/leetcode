# https://leetcode.com/problems/minimum-distance-between-bst-nodes/ 

class Solution(object):
	def minDiffInBST(self, root):
		nodes = []
		stack = [root]
		while stack:
			u = stack.pop()
			if u:
				nodes.append(u.val)
				stack.append(u.left)
				stack.append(u.right)

		nodes = sorted(nodes)
		res = float('inf')
		for i in range(1, len(nodes)):
			res = min(res, nodes[i] - nodes[i - 1])
            
		return res
